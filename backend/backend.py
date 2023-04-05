from database import Database
from utils import Utils
from options import Options
from games import Games
from users import Users
from specialists import Specialists
from admins import Admins
from betsh2h import BetsH2H
import threading
import codes
import time


class Backend():

	def __init__(self, db_name="sql.db"):
		self.db = Database(db_name)
		self.utils = Utils(db_name=db_name)
		self.options = Options(db_name=db_name)
		self.games = Games(db_name=db_name)
		self.users = Users(self.games, self.utils, db_name=db_name)
		self.specialists = Specialists(db_name=db_name)
		self.admins = Admins(db_name=db_name)
		self.betsh2h = BetsH2H(self.users, self.games, self.options, self.utils, db_name=db_name)


	def reset_users(self): return self.users.reset_users()


	def reset_specialists(self): return self.specialists.reset_specialists()


	def reset_admins(self): return self.admins.reset_admins()


	def reset_options(self): return self.options.reset_options()


	def reset_games(self): return self.games.reset_games()


	def register(self, table, nif, username, email, password):
		# Verify data
		if not self.utils.verify_nif(nif):		     return codes.NIF_ERROR,None
		if not self.utils.verify_password(password): return codes.PASSWORD_ERROR,None
		if not self.utils.verify_username(username): return codes.USERNAME_ERROR,None
		if not self.utils.verify_email(email):       return codes.EMAIL_ERROR,None

		results = self.utils.exists_nif(nif)
		if results != codes.VALID:
			return results, None

		# Verify if username or email exists in database
		results = self.utils.exists_username_email(username, email)
		if results != codes.VALID:
			return results, None

		# Add user to database
		password = self.utils.hash(password)
		if table == "USERS": 
			return self.users.register_user(nif, username, email, password)
		elif table == "SPECIALISTS": 
			return self.specialists.register_specialist(nif, username, email, password)
		elif table == "ADMINS":
			return self.admins.register_admin(nif, username, email, password)
		return codes.ERROR, None



	def login(self, user_or_email, password):
		password = self.utils.hash(password)
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM USERS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				return codes.VALID_USER, results[0][2]
			else:
				return codes.PASSWORD_ERROR, None
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM SPECIALISTS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				return codes.VALID_SPECIALIST, results[0][2]
			else:
				return codes.PASSWORD_ERROR, None
		results = self.db.execute(
			''' SELECT USERNAME, PASSWORD, NIF FROM ADMINS WHERE (USERNAME='{}' OR EMAIL='{}') '''
			.format(user_or_email, user_or_email))
		if len(results) == 1:
			if results[0][1] == password:
				return codes.VALID_ADMIN, results[0][2]
			else:
				return codes.PASSWORD_ERROR, None
		return codes.USERNAME_ERROR, None


	def get_username(self, nif, table): return self.utils.get_username(nif, table)


	def send_notification(self, nif, text):
		state = self.options.get_value("NOTIFICATIONS_STATE")
		if state != "TRUE": return
		self.users.send_notification(nif, text)


	def get_notifications(self, nif): return self.users.get_notifications(nif)


	def edit_profile(self, nif, username, email, password): return self.users.edit_profile(nif, username, email, password)


	def get_user_data(self, nif): return self.users.get_user_data(nif)


	def withdraw_money(self, nif, amount): return self.users.withdraw_money(nif, amount)


	def deposit_money(self, nif, amount): return self.users.deposit_money(nif, amount)


	def bet(self, nif, game_ids, beted_results, amount): return self.betsh2h.bet(nif, game_ids, beted_results, amount)


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
			self.games.update_games()
			self.betsh2h.update_bets()
			time.sleep(time_interval)


	def cash_out(self, nif, bet_id): return self.users.cash_out(nif, bet_id)


	def bet_history(self, nif): return self.users.bet_history(nif)


	def transaction_history(self, nif): return self.users.transaction_history(nif)
	

	def notify_all(self, message): return self.users.notify_all(message)


	def check_follows_game(self, nif, game_id): return self.users.check_follows_game(nif, game_id)


	def follow_game(self, nif, game_id): return self.users.follow_game(nif, game_id)


	def unfollow_game(self, nif, game_id): return self.users.unfollow_game(nif, game_id)


	def get_options(self): return self.options.get_options()


	def set_option(self, option, value): return self.options.set_option(option, value)


	def get_games(self, sport, state="ANY"): return self.games.get_games(sport, state=state)


	def get_games_and_outcomes(self, sport): return self.games.get_games_and_outcomes(sport)


	def set_games_odds(self, sport, ids, odds):
		for i in ids: self.users.notify_about_game(i)
		return self.games.set_games_odds(sport, ids, odds)


	def set_games_states(self, sport, ids, states): return self.games.set_games_states(sport, ids, states)


	def set_api_timeout(self, timeout): self.games.api_timeout = timeout