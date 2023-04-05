from database import Database
import threading
import datetime
import time
import re


class Backend():

	VALID            = "valid"
	PASSWORD_ERROR   = "password_error"
	USERNAME_ERROR   = "username_error"
	EMAIL_ERROR      = "email_error"
	EMAIL_TAKEN      = "email_taken"
	USERNAME_TAKEN   = "username_taken"
	NIF_ERROR        = "nif_error"
	NIF_TAKEN        = "nif_taken"
	VALID_USER       = "valid_user"
	VALID_SPECIALIST = "valid_specialist"
	VALID_ADMIN      = "valid_admin"
	INVALID_AMOUNT   = "invalid_amount"
	BET_ERROR        = "bet_error"
	ERROR            = "error"


	def __init__(self,game_db,database_name="sql.db"):
		self.game_db = game_db
		self.db = Database(database_name)


	def exists_username_email(self, username, email, nif=""):
		results = self.db.execute(
			''' SELECT NIF, USERNAME, EMAIL FROM USERS WHERE USERNAME='{}' OR EMAIL='{}' '''
			.format(username, email)) + self.db.execute(
			''' SELECT NIF, USERNAME, EMAIL FROM SPECIALISTS WHERE USERNAME='{}' OR EMAIL='{}' '''
			.format(username, email)) + self.db.execute(
			''' SELECT NIF, USERNAME, EMAIL FROM ADMINS WHERE USERNAME='{}' OR EMAIL='{}' '''
			.format(username, email))
		if len(results) > 0:
			for result in results:
				if result[0] != nif:
					if result[1] == username:
						return self.USERNAME_TAKEN
					else: return self.EMAIL_TAKEN
		return self.VALID


	def exists_nif_user(self, nif):
		results = self.db.execute(
			''' SELECT NIF FROM USERS WHERE NIF='{}' '''.format(nif)
		)
		if len(results) > 0:
			return self.VALID
		return self.NIF_ERROR


	def hash(self, text:str):
		#return text
		hash=0
		for ch in text:
			hash = ( hash*281  ^ ord(ch)*997) & 0xFFFFFFFF
		return str(hash)
	

	def exists_nif(self, nif):
		results = self.db.execute(
			''' SELECT NIF FROM USERS WHERE NIF='{}' '''.format(nif)
		) + self.db.execute(
			''' SELECT NIF FROM SPECIALISTS WHERE NIF='{}' '''.format(nif)
		) + self.db.execute(
			''' SELECT NIF FROM ADMINS WHERE NIF='{}' '''.format(nif)
		)

		if len(results) > 0:
			return self.NIF_TAKEN

		return self.VALID


	def reset_options(self):
		db_name = "OPTIONS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NAME      TEXT     PRIMARY KEY   NOT NULL,
	          VALUE     TEXT                   NOT NULL);
	         '''.format(db_name))
		self.db.execute('''INSERT INTO OPTIONS VALUES ('NOTIFICATIONS_STATE', 'TRUE')''')
		self.db.execute('''INSERT INTO OPTIONS VALUES ('PROMOTIONS_STATE',    'TRUE')''')
		self.db.execute('''INSERT INTO OPTIONS VALUES ('PROMOTIONS_LIMIT',    '50')  ''')
		self.db.execute('''INSERT INTO OPTIONS VALUES ('PROMOTIONS_BONUS',    '5')   ''')
		print("Options Table initialized")
		return self.VALID


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
		return self.VALID
	

	def reset_specialists(self):
		db_name = "SPECIALISTS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NIF   VARCHAR(9)   PRIMARY KEY   NOT NULL,
			 USERNAME            VARCHAR(24)   NOT NULL,
	         EMAIL               VARCHAR(24)   NOT NULL,
	         PASSWORD            TEXT          NOT NULL,
	         UNIQUE (NIF, USERNAME, EMAIL));
	         '''.format(db_name))
		
		print("Specialists Table initialized")
		return self.VALID


	def reset_admins(self):
		db_name = "ADMINS"
		self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
		self.db.execute('''CREATE TABLE {}
	         (NIF   VARCHAR(9)   PRIMARY KEY   NOT NULL,
			 USERNAME            VARCHAR(24)   NOT NULL,
	         EMAIL               VARCHAR(24)   NOT NULL,
	         PASSWORD            TEXT          NOT NULL,
	         UNIQUE (NIF, USERNAME, EMAIL));
	         '''.format(db_name))
		
		print("Admins Table initialized")
		return self.VALID


	def verify_password(self, password):
		if len(password) > 24 or len(password) < 6: return False
		contains_forbidden_chars = any([c in "\n\t " for c in password])
		contains_num_chars       = any([c in "1234567890" for c in password])
		#contains_special_chars   = any([c in "_.:?=[]{}()/\\!@$%^&*<>|~" for c in password])
		contains_caps_chars      = any([c.isupper() for c in password])
		contains_lower_chars     = any([c.islower() for c in password])
		if contains_caps_chars and contains_lower_chars and not contains_forbidden_chars and contains_num_chars:
			return True
		return False


	def verify_username(self, username):
		if len(username) > 24: return False
		contains_forbidden_chars = any([c in "\n\t " for c in username])
		if contains_forbidden_chars: return False
		return True


	def verify_email(self, email):
		if re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
			return True
		return False


	def verify_nif(self, nif):
		if len(nif) == 9 and re.fullmatch(r"[0-9]+", nif):
			return True
		return False


	def register(self, table, nif, username, email, password):
		# Verify data
		if not self.verify_nif(nif):		   return self.NIF_ERROR,None
		if not self.verify_password(password): return self.PASSWORD_ERROR,None
		if not self.verify_username(username): return self.USERNAME_ERROR,None
		if not self.verify_email(email):       return self.EMAIL_ERROR,None

		results = self.exists_nif(nif)
		if results != self.VALID:
			return results,None
		# Verify if username or email exists in database
		results = self.exists_username_email(username, email)
		if results != self.VALID:
			return results,None

		# Add user to database
		password = self.hash(password)
		if table == "USERS": 
			self.db.execute(
				''' INSERT INTO USERS VALUES ('{}', '{}', '{}', '{}', 0.0, 0, 0.0) '''
				.format(nif, username, email, password))
			self.send_notification(nif,"Bem-vindo à RASBET!")
			
			return self.VALID_USER, nif
		elif table == "SPECIALISTS": 
			self.db.execute(
				''' INSERT INTO SPECIALISTS VALUES ('{}', '{}', '{}', '{}') '''
				.format(nif, username, email, password))
			
			return self.VALID_SPECIALIST, nif
		elif table == "ADMINS":
			self.db.execute(
				''' INSERT INTO ADMINS VALUES ('{}', '{}', '{}', '{}') '''
				.format(nif, username, email, password))
			
			return self.VALID_ADMIN, nif
		return self.ERROR, None


	def login(self, user_or_email, password):
		password = self.hash(password)
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM USERS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				self.send_notification(user_or_email,"Bem-vindo de volta!")
				return self.VALID_USER, results[0][2]
			else:
				return self.PASSWORD_ERROR, None
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM SPECIALISTS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				return self.VALID_SPECIALIST, results[0][2]
			else:
				return self.PASSWORD_ERROR, None
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM ADMINS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				return self.VALID_ADMIN, results[0][2]
			else:
				return self.PASSWORD_ERROR, None
		return self.USERNAME_ERROR, None


	def get_username(self, nif, table):
		usernames = self.db.execute('''
				SELECT USERNAME FROM {} WHERE NIF='{}'
			'''.format(table, nif))
		if len(usernames) == 0: return None
		return usernames[0][0]


	def send_notification(self, nif, text):
		state = self.db.execute('''
				SELECT VALUE FROM OPTIONS WHERE NAME='NOTIFICATIONS_STATE' AND VALUE='TRUE'
			''')
		if len(state) == 0: return
		self.db.execute('''
				INSERT INTO NOTIFICATIONS (NIF, TEXT, SEEN) VALUES ('{}', '{}', 'NO')
			'''.format(nif, text))


	def get_notifications(self, nif):
		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR, []
		
		notifications = self.db.execute('''
				SELECT ID, TEXT, SEEN FROM NOTIFICATIONS WHERE NIF='{}'
			'''.format(nif))

		for n in notifications:
			self.db.execute('''
					UPDATE NOTIFICATIONS SET SEEN='YES' WHERE ID={}
				'''.format(n[0]))

		return self.VALID, notifications


	def edit_profile(self, nif, username, email, password):
		# Verify data
		if len(password) > 0 and not self.verify_password(password): return self.PASSWORD_ERROR
		if not self.verify_username(username): return self.USERNAME_ERROR
		if not self.verify_email(email):       return self.EMAIL_ERROR

		# Verify if username or email exists in database
		results = self.exists_username_email(username, email, nif=nif)
		if results != self.VALID:
			return results

		if len(password) > 0:
			password = self.hash(password)
			self.db.execute(
				''' UPDATE USERS SET USERNAME='{}', EMAIL='{}', PASSWORD='{}' WHERE NIF='{}' '''.format(username, email, password, nif)
			)
		else:
			self.db.execute(
				''' UPDATE USERS SET USERNAME='{}', EMAIL='{}' WHERE NIF='{}' '''.format(username, email, nif)
			)
		
		return self.VALID


	def get_user_data(self, nif):
		users = self.db.execute('''
				SELECT NIF, USERNAME, EMAIL, PASSWORD, WALLET FROM USERS WHERE NIF='{}'
			'''.format(nif))
		if len(users) > 0:
			return self.VALID, users[0]
		return self.NIF_ERROR, []


	def withdraw_money(self, nif, amount):
		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR
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
				
				return self.VALID
		return self.INVALID_AMOUNT


	def deposit_money(self, nif, amount):
		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR
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
			
			return self.VALID
		return self.INVALID_AMOUNT


	def check_promotion(self, nif, amount):
		state = self.db.execute('''
				SELECT VALUE FROM OPTIONS WHERE NAME='PROMOTIONS_STATE'
			''')
		if len(state) == 0 or state[0][0] != "TRUE": return

		betted_amount_counter = self.db.execute('''
				SELECT BETTED_AMOUNT_COUNTER FROM USERS WHERE NIF='{}'
			'''.format(nif))[0][0] + amount

		self.db.execute('''
				UPDATE USERS SET BETTED_AMOUNT_COUNTER={} WHERE NIF='{}'
			'''.format(betted_amount_counter, nif))

		promotion_limit = float(self.db.execute('''
				SELECT VALUE FROM OPTIONS WHERE NAME='PROMOTIONS_LIMIT'
			''')[0][0])

		if betted_amount_counter < promotion_limit: return

		self.db.execute('''
				UPDATE USERS SET BETTED_AMOUNT_COUNTER={} WHERE NIF='{}'
			'''.format(betted_amount_counter - promotion_limit, nif))

		promotion_bonus = float(self.db.execute('''
				SELECT VALUE FROM OPTIONS WHERE NAME='PROMOTIONS_BONUS'
			''')[0][0])

		# Give bonus
		wallet_amount = self.db.execute('''
				SELECT WALLET FROM USERS WHERE NIF='{}'
			'''.format(nif))[0][0]

		self.db.execute('''
				UPDATE USERS SET WALLET={} WHERE NIF='{}'
			'''.format(wallet_amount + promotion_bonus, nif))

		self.db.execute('''
				INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'BONUS', '{}')
			'''.format(nif, promotion_bonus, datetime.datetime.now()))




	def bet(self, nif, game_ids, beted_results, amount):
		game_ids      = game_ids[:min(len(game_ids), 20)]
		beted_results = beted_results[:min(len(beted_results), 20)]

		# Check constraints
		if self.exists_nif_user(nif) == self.NIF_ERROR or len(game_ids) != len(beted_results) or len(game_ids)==0:
			return self.BET_ERROR
		current_amount = self.db.execute(
			''' SELECT WALLET FROM USERS WHERE NIF='{}' '''.format(nif)
		)[0][0]
		if current_amount < amount or amount <= 1.0:
			return self.INVALID_AMOUNT
		available_bets = [1,2,0]
		for i in range(len(game_ids)):
			if self.game_db.get_game(game_ids[i]) == None or not beted_results[i] in available_bets:
				return self.BET_ERROR

		# Remove money
		self.db.execute('''
				UPDATE USERS SET WALLET={} WHERE NIF='{}'
			'''.format(current_amount-amount, nif)
		)
		self.db.execute('''
				INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'BET', '{}')
			'''.format(nif, amount, datetime.datetime.now()))

		# Update bet counter
		counter = self.db.execute('''
				SELECT BET_COUNTER FROM USERS WHERE NIF='{}'
			'''.format(nif))[0][0]
		self.db.execute('''
				UPDATE USERS SET BET_COUNTER={} WHERE NIF='{}'
			'''.format(counter + 1, nif))

		self.check_promotion(nif, amount)

		# Add simple_bets
		final_odd = 1
		for i in range(len(game_ids)):
			final_odd = final_odd * self.game_db.get_odd(game_ids[i], beted_results[i])
			self.db.execute('''
					INSERT INTO SIMPLE_BET VALUES ({}, {}, '{}', {}, 'WAIT', '{}')
				'''.format(i+1, counter + 1, game_ids[i], beted_results[i], nif))

		# Add main_bet
		self.db.execute('''
				INSERT INTO MAIN_BET VALUES ({}, {}, '{}', {}, {}, '{}', 'WAIT')
			'''.format(counter + 1, amount, nif, len(game_ids), final_odd, datetime.datetime.now()))
		
		return self.VALID


	def start_update_cycle(self, time_interval=30):
		self.cycle_thread = threading.Thread(target=self.games_cycle, args=(time_interval,))
		self.cycle_thread.daemon = True
		self.cycle_thread.start()
		pass


	def join_update_cycle(self):
		while self.cycle_thread.is_alive():
			self.cycle_thread.join(1)
			time.sleep(1)


	def games_cycle(self, time_interval=30):
		while True:
			self.game_db.update_games()
			self.update_bets()
			time.sleep(time_interval)


	def update_bets(self):
		all_simple = self.db.execute('''
    			SELECT MAIN_BET, GAME_ID, STATE, ID, BETED_RESULT, NIF FROM SIMPLE_BET WHERE STATE='WAIT'
    		''')

		for bet in all_simple:
			completed = self.game_db.is_running(bet[1])
			if completed == "TRUE":
				score = self.game_db.get_score(bet[1])
				state = "LOSS"
				h = int(score[0])
				a = int(score[2])
				if bet[4] == 0 and h > a: state = "WIN"
				if bet[4] == 1 and h == a: state = "WIN"
				if bet[4] == 2 and h < a: state = "WIN"

				self.db.execute('''
    					UPDATE SIMPLE_BET SET STATE='{}' WHERE ID={} AND MAIN_BET={} AND NIF='{}'
    				'''.format(state, bet[3], bet[0], bet[5]))

		all_main = self.db.execute('''
			SELECT ID, AMOUNT, NIF, FINAL_ODD, STATE FROM MAIN_BET WHERE STATE='WAIT'
		''')

		for bet in all_main:
			all_simple = self.db.execute('''
	    			SELECT STATE FROM SIMPLE_BET WHERE MAIN_BET={} AND NIF='{}'
	    		'''.format(bet[0], bet[2]))

			if len(all_simple) == 0: continue

			completed = not any([b[0] == "WAIT" for b in all_simple])

			if completed:
				state = not any([b[0] == "LOSS" for b in all_simple])
				if state:
					self.db.execute('''
    						UPDATE MAIN_BET SET STATE='WIN' WHERE NIF='{}' AND ID={}
    					'''.format(bet[2], bet[0]))
					win_amount = bet[1] * bet[3]
					wallet_amount = self.db.execute('''
						SELECT WALLET FROM USERS WHERE NIF='{}'
					'''.format(bet[2]))[0][0]
					self.db.execute('''
						UPDATE USERS SET WALLET={} WHERE NIF='{}'
					'''.format(wallet_amount + win_amount, bet[2]))
					self.db.execute('''
						INSERT INTO TRANSACTIONS VALUES ('{}', {}, 'BET_WIN', '{}')
					'''.format(bet[2], win_amount, datetime.datetime.now()))
					self.send_notification(bet[2],f"Parabéns, ganhou {win_amount}€ numa aposta!")
				else:
					self.send_notification(bet[2],"Que pena..Perdeu a sua aposta!")
					self.db.execute('''
    						UPDATE MAIN_BET SET STATE='LOSS' WHERE NIF='{}' AND ID={}
    					'''.format(bet[2], bet[0]))


	def cash_out(self, nif, bet_id):
		
		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR

		main_bet = self.db.execute('''
				SELECT AMOUNT FROM MAIN_BET WHERE STATE='WAIT' AND ID={} AND NIF='{}'
			'''.format(bet_id, nif))

		if len(main_bet) == 0: return self.BET_ERROR

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
		return self.VALID


	def bet_history(self, nif):

		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR, []

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
				game = list(self.game_db.get_game(sb[0]))
				new_mb[-1].append([game[1], game[2], game[3], sb[1], sb[2]])
			main_bets_final.append(new_mb)
		print(">>>>", main_bets_final)
		return self.VALID, main_bets_final


	def transaction_history(self, nif):

		if self.exists_nif_user(nif) == self.NIF_ERROR:
			return self.NIF_ERROR, []

		transactions = self.db.execute('''
				SELECT AMOUNT, TYPE, DATE FROM TRANSACTIONS WHERE NIF='{}'
			'''.format(nif))

		return self.VALID, transactions
	
	def notify_all(self, message):
		nifs =self.db.execute('''
			SELECT NIF FROM USERS
			''' )
		for nif in nifs:
			self.send_notification(nif[0],message)
		return self.VALID


	def notify_about_game(self, game_id):
		nifs_beted = self.db.execute('''
				SELECT NIF FROM SIMPLE_BET WHERE GAME_ID='{}'
			'''.format(game_id))
		nifs_follow = self.db.execute('''
				SELECT NIF FROM GAME_FOLLOW WHERE GAME_ID='{}'
			'''.format(game_id))
		nifs = nifs_beted + nifs_follow
		nifs = [*set([x[0] for x in nifs])]
		game = self.game_db.get_game(game_id)
		for nif in nifs:
			self.send_notification(nif, f"Odds of {game[1]} vs {game[2]} game changed!")

	def check_follows_game(self, nif, game_id):
		items = self.db.execute('''
				SELECT * FROM GAME_FOLLOW WHERE NIF='{}' AND GAME_ID='{}'
			'''.format(nif, game_id))
		if len(items) > 0: return self.VALID, "true"
		return self.VALID, "false"

	def follow_game(self, nif, game_id):
		self.db.execute('''
				INSERT INTO GAME_FOLLOW VALUES ('{}', '{}')
			'''.format(nif, game_id))
		return self.VALID


	def unfollow_game(self, nif, game_id):
		self.db.execute('''
				DELETE FROM GAME_FOLLOW WHERE NIF='{}' AND GAME_ID='{}'
			'''.format(nif, game_id))
		return self.VALID


	def get_options(self):
		options = self.db.execute('''
				SELECT * FROM OPTIONS
			''')
		return self.VALID, options


	def set_option(self, option, value):
		self.db.execute('''
				UPDATE OPTIONS SET VALUE='{}' WHERE NAME='{}'
			'''.format(value, option))
		return self.VALID