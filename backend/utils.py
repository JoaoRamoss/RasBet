import re
import codes
from database import Database


class Utils():

	def __init__(self, db_name):
		self.db = Database(db_name)


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
						return codes.USERNAME_TAKEN
					else: return codes.EMAIL_TAKEN
		return codes.VALID


	def exists_nif_user(self, nif):
		results = self.db.execute(
			''' SELECT NIF FROM USERS WHERE NIF='{}' '''.format(nif)
		)
		if len(results) > 0:
			return codes.VALID
		return codes.NIF_ERROR


	def hash(self, text:str):
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
			return codes.NIF_TAKEN
		return codes.VALID


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


	def get_username(self, nif, table):
		usernames = self.db.execute('''
				SELECT USERNAME FROM {} WHERE NIF='{}'
			'''.format(table, nif))
		if len(usernames) == 0: return None
		return usernames[0][0]