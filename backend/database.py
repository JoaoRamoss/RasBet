# NEW

import sqlite3

print(sqlite3.sqlite_version)

class Database():

	def __init__(self, name="sql.db"):
		self.name = name

	def execute(self, query):
		try:
			db = sqlite3.connect(self.name, check_same_thread=False)
			cursor = db.cursor()
			cursor.execute(query)
			result = cursor.fetchall()
			return result
		except sqlite3.Error as error:
			print("Error on Query SQLite:{}".format(error))
		finally:
			cursor.close()
			db.commit()
			db.close()
		return []