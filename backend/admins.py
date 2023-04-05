from database import Database
import codes


class Admins():

	def __init__(self, db_name="sql.db"):
		self.db = Database(db_name)


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
		return codes.VALID


	def register_admin(self, nif, username, email, password):
		# Add to the database
		self.db.execute(
			''' INSERT INTO ADMINS VALUES ('{}', '{}', '{}', '{}') '''
			.format(nif, username, email, password))
		
		return codes.VALID_ADMIN, nif