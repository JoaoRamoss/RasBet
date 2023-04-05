from database import Database
import datetime
import codes
import time
import re


class Users():

	def __init__(self, games, utils, db_name="sql.db"):
		self.db    = Database(db_name)
		self.utils = utils
		self.games = games


	def reset_users(self):
		db_name = "USERS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NIF   VARCHAR(9)     PRIMARY KEY   NOT NULL,
			 USERNAME              VARCHAR(24)   NOT NULL,
	         EMAIL                 VARCHAR(24)   NOT NULL,
	         PASSWORD              TEXT          NOT NULL,
	         WALLET                REAL          NOT NULL,
	         BET_COUNTER           INT           NOT NULL,
	         BETTED_AMOUNT_COUNTER REAL          NOT NULL,
	         UNIQUE (NIF, USERNAME, EMAIL));
	         '''.format(db_name))
		
		db_name = "NOTIFICATIONS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	         NIF                 VARCHAR(9)    NOT NULL,
			 TEXT                TEXT          NOT NULL,
	         SEEN                VARCHAR(3)    NOT NULL CHECK(SEEN='YES' OR SEEN='NO'),
	         UNIQUE (ID));
	         '''.format(db_name))
		
		db_name = "GAME_FOLLOW"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NIF                VARCHAR(9)    NOT NULL,
	          GAME_ID            VARCHAR(32)   NOT NULL);
	         '''.format(db_name))
		
		db_name = "TRANSACTIONS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NIF                VARCHAR(9)    NOT NULL,
	         AMOUNT              REAL          NOT NULL,
	         TYPE                VARCHAR(8)    NOT NULL CHECK(TYPE='DEPOSIT' OR TYPE='WITHDRAW' OR TYPE='BET' OR TYPE='BET_WIN' OR TYPE='CASH_OUT' OR TYPE='BONUS'),
	         DATE                TEXT          NOT NULL);
	         '''.format(db_name))
		
		db_name = "MAIN_BET"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (ID       INT      PRIMARY KEY   NOT NULL,
			 AMOUNT    REAL                   NOT NULL,
	         NIF       VARCHAR(9)             NOT NULL,
	         COUNT     INT                    NOT NULL,
	         FINAL_ODD REAL                   NOT NULL,
			 DATE      TEXT                   NOT NULL,
			 STATE     VARCHAR(5)             NOT NULL CHECK(STATE='WIN' OR STATE='LOSS' OR STATE='WAIT' OR STATE='CASHED_OUT'));
	         '''.format(db_name))
		
		db_name = "SIMPLE_BET"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (ID                INTEGER      NOT NULL,
			 MAIN_BET           INT          NOT NULL,
	         GAME_ID            VARCHAR(32)  NOT NULL,
	         BETED_RESULT       INT          NOT NULL,
	         STATE              VARCHAR(5)   NOT NULL CHECK(STATE='WIN' OR STATE='LOSS' OR STATE='WAIT' OR STATE='CASHED_OUT'),
	         NIF                VARCHAR(9)   NOT NULL);  
	         '''.format(db_name))
		
		print("Users Table initialized")
		return codes.VALID


	def register_user(self, nif, username, email, password):
		# Add to the database
		self.db.execute(
			''' INSERT INTO USERS VALUES ('{}', '{}', '{}', '{}', 0.0, 0, 0.0) '''
			.format(nif, username, email, password))

		# Welcome notification
		self.send_notification(nif,"Bem-vindo à RASBET!")
		
		return codes.VALID_USER, nif


	def send_notification(self, nif, text):
		self.db.execute('''
				INSERT INTO NOTIFICATIONS (NIF, TEXT, SEEN) VALUES ('{}', '{}', 'NO')
			'''.format(nif, text))


	def get_notifications(self, nif):
		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR, []
		
		notifications = self.db.execute('''
				SELECT ID, TEXT, SEEN FROM NOTIFICATIONS WHERE NIF='{}'
			'''.format(nif))

		for n in notifications:
			self.db.execute('''
					UPDATE NOTIFICATIONS SET SEEN='YES' WHERE ID={}
				'''.format(n[0]))

		return codes.VALID, notifications


	def edit_profile(self, nif, username, email, password):
		# Verify data
		if len(password) > 0 and not self.utils.verify_password(password): return codes.PASSWORD_ERROR
		if not self.utils.verify_username(username): return codes.USERNAME_ERROR
		if not self.utils.verify_email(email):       return codes.EMAIL_ERROR

		# Verify if username or email exists in database
		results = self.utils.exists_username_email(username, email, nif=nif)
		if results != codes.VALID:
			return results

		if len(password) > 0:
			password = self.utils.hash(password)
			self.db.execute(
				''' UPDATE USERS SET USERNAME='{}', EMAIL='{}', PASSWORD='{}' WHERE NIF='{}' '''.format(username, email, password, nif)
			)
		else:
			self.db.execute(
				''' UPDATE USERS SET USERNAME='{}', EMAIL='{}' WHERE NIF='{}' '''.format(username, email, nif)
			)
		
		return codes.VALID


	def get_user_data(self, nif):
		users = self.db.execute('''
				SELECT NIF, USERNAME, EMAIL, PASSWORD, WALLET FROM USERS WHERE NIF='{}'
			'''.format(nif))
		if len(users) > 0:
			return codes.VALID, users[0]
		return codes.NIF_ERROR, []


	def withdraw_money(self, nif, amount):
		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR
		if amount > 0.0:
			current_amount = self.db.execute(
				''' SELECT WALLET FROM USERS WHERE NIF='{}' '''.format(nif)
			)[0][0]
			new_amount = current_amount - float(amount)
			if new_amount >= 0.0:
				self.db.execute(
					''' UPDATE USERS SET WALLET='{}' WHERE NIF='{}' '''.format(new_amount, nif)
				)
				self.db.execute('''
						INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'WITHDRAW', '{}')
					'''.format(nif, amount, datetime.datetime.now()))
				
				return codes.VALID
		return codes.INVALID_AMOUNT


	def deposit_money(self, nif, amount):
		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR
		if amount > 0.0:
			current_amount = self.db.execute(
				''' SELECT WALLET FROM USERS WHERE NIF='{}' '''.format(nif)
			)[0][0]
			new_amount = current_amount + float(amount)
			self.db.execute(
				''' UPDATE USERS SET WALLET='{}' WHERE NIF='{}' '''.format(new_amount, nif)
			)
			self.db.execute('''
						INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'DEPOSIT', '{}')
					'''.format(nif, amount, datetime.datetime.now()))
			
			return codes.VALID
		return codes.INVALID_AMOUNT


	def cash_out(self, nif, bet_id):
		
		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR

		main_bet = self.db.execute('''
				SELECT AMOUNT FROM MAIN_BET WHERE STATE='WAIT' AND ID={} AND NIF='{}'
			'''.format(bet_id, nif))

		if len(main_bet) == 0: return codes.BET_ERROR

		amount = main_bet[0][0]

		current_amount = self.db.execute('''
				SELECT WALLET FROM USERS WHERE NIF='{}'
			'''.format(nif))[0][0]

		self.db.execute('''
				UPDATE USERS SET WALLET={} WHERE NIF='{}'
			'''.format(current_amount + (amount / 2), nif))
		self.db.execute('''
				INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'CASH_OUT', '{}')
			'''.format(nif, amount / 2, datetime.datetime.now()))

		self.db.execute('''
				UPDATE MAIN_BET SET STATE='CASHED_OUT' WHERE ID={} AND NIF='{}'
			'''.format(bet_id, nif))
		return codes.VALID


	def bet_history(self, nif):

		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR, []

		main_bets = self.db.execute('''
				SELECT ID, AMOUNT, FINAL_ODD, DATE, STATE FROM MAIN_BET WHERE NIF='{}'
			'''.format(nif))

		main_bets_final = []
		for mb in main_bets:
			simple_bets = self.db.execute('''
					SELECT GAME_ID, BETED_RESULT, STATE FROM SIMPLE_BET WHERE MAIN_BET={} AND NIF='{}'
				'''.format(mb[0], nif))

			print("MB", mb)
			print("simple_bets", simple_bets)
			new_mb = list(mb)
			new_mb.append([])
			for sb in simple_bets:
				game = list(self.games.get_game(sb[0]))
				new_mb[-1].append([game[1], game[2], game[3], sb[1], sb[2]])
			main_bets_final.append(new_mb)
		print(">>>>", main_bets_final)
		return codes.VALID, main_bets_final


	def transaction_history(self, nif):

		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR:
			return codes.NIF_ERROR, []

		transactions = self.db.execute('''
				SELECT AMOUNT, TYPE, DATE FROM TRANSACTIONS WHERE NIF='{}'
			'''.format(nif))

		return codes.VALID, transactions
	
	def notify_all(self, message):
		nifs = self.db.execute('''
			SELECT NIF FROM USERS
			''' )
		for nif in nifs:
			self.send_notification(nif[0], message)
		return codes.VALID


	def notify_about_game(self, game_id):
		nifs_beted = self.db.execute('''
				SELECT NIF FROM SIMPLE_BET WHERE GAME_ID='{}'
			'''.format(game_id))
		nifs_follow = self.db.execute('''
				SELECT NIF FROM GAME_FOLLOW WHERE GAME_ID='{}'
			'''.format(game_id))
		nifs = nifs_beted + nifs_follow
		nifs = [*set([x[0] for x in nifs])]
		game = self.games.get_game(game_id)
		for nif in nifs:
			self.send_notification(nif, f"Odds of {game[1]} vs {game[2]} game changed!")


	def check_follows_game(self, nif, game_id):
		items = self.db.execute('''
				SELECT * FROM GAME_FOLLOW WHERE NIF='{}' AND GAME_ID='{}'
			'''.format(nif, game_id))
		if len(items) > 0: return codes.VALID, "true"
		return codes.VALID, "false"


	def follow_game(self, nif, game_id):
		self.db.execute('''
				INSERT INTO GAME_FOLLOW VALUES ('{}', '{}')
			'''.format(nif, game_id))
		return codes.VALID


	def unfollow_game(self, nif, game_id):
		self.db.execute('''
				DELETE FROM GAME_FOLLOW WHERE NIF='{}' AND GAME_ID='{}'
			'''.format(nif, game_id))
		return codes.VALID