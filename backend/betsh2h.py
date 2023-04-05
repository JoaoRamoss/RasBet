from database import Database
import datetime
import codes


class BetsH2H():

	def __init__(self, users, games, options, utils, db_name="sql.db"):
		self.db = Database(db_name)
		self.games = games
		self.options = options
		self.utils = utils


	def check_promotion(self, nif, amount):
		state = self.options.get_value("PROMOTIONS_STATE")
		if state != "TRUE": return

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
		if self.utils.exists_nif_user(nif) == codes.NIF_ERROR or len(game_ids) != len(beted_results) or len(game_ids)==0:
			return codes.BET_ERROR
		current_amount = self.db.execute(
			''' SELECT WALLET FROM USERS WHERE NIF='{}' '''.format(nif)
		)[0][0]
		if current_amount < amount or amount <= 1.0:
			return codes.INVALID_AMOUNT
		available_bets = [1,2,0]
		for i in range(len(game_ids)):
			if self.games.get_game(game_ids[i]) == None or not beted_results[i] in available_bets:
				return codes.BET_ERROR

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
			final_odd = final_odd * self.games.get_odd(game_ids[i], beted_results[i])
			self.db.execute('''
					INSERT INTO SIMPLE_BET VALUES ({}, {}, '{}', {}, 'WAIT', '{}')
				'''.format(i+1, counter + 1, game_ids[i], beted_results[i], nif))

		# Add main_bet
		self.db.execute('''
				INSERT INTO MAIN_BET VALUES ({}, {}, '{}', {}, {}, '{}', 'WAIT')
			'''.format(counter + 1, amount, nif, len(game_ids), final_odd, datetime.datetime.now()))
		
		return codes.VALID




	def update_bets(self):
		all_simple = self.db.execute('''
    			SELECT MAIN_BET, GAME_ID, STATE, ID, BETED_RESULT, NIF FROM SIMPLE_BET WHERE STATE='WAIT'
    		''')

		for bet in all_simple:
			completed = self.games.is_running(bet[1])
			if completed == "TRUE":
				score = self.games.get_score(bet[1])
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
					self.users.send_notification(bet[2], f"Parabéns, ganhou {win_amount}€ numa aposta!")
				else:
					self.users.send_notification(bet[2], "Que pena..Perdeu a sua aposta!")
					self.db.execute('''
    						UPDATE MAIN_BET SET STATE='LOSS' WHERE NIF='{}' AND ID={}
    					'''.format(bet[2], bet[0]))