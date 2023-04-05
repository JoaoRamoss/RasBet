from database import Database
import codes

class Options():

	def __init__(self, db_name="sql.db"):
		self.db = Database(db_name)


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
		return codes.VALID


	def get_value(self, name):
		state = self.db.execute('''
				SELECT VALUE FROM OPTIONS WHERE NAME='{}'
			'''.format(name))
		if len(state) == 0: return ""
		else: return state[0][0]


	def get_options(self):
		options = self.db.execute('''
				SELECT * FROM OPTIONS
			''')
		return codes.VALID, options


	def set_option(self, option, value):
		self.db.execute('''
				UPDATE OPTIONS SET VALUE='{}' WHERE NAME='{}'
			'''.format(value, option))
		return codes.VALID