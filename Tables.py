import sqlite3
class Data_base:
	def __init__(self, db):
		self.db = db
		self.conn = None
		self.cursor = None

	def connect(self):
		self.conn = sqlite3.connect(self.db)
		self.cursor = self.conn.cursor()

	def close(self):
		if self.conn:
			self.conn.close()

	def execute_query(self, query, params=None):
		if params is None:
			self.cursor.execute(query)
		else:
			self.cursor.execute(query, params) #tupla?
		self.conn.commit()

	def fetch_query(self, query, params=None):
		if params is None:
			self.cursor.execute(query)
		else:
			self.cursor.execute(query, params)
		return self.cursor.fetchall()

	def fetch_one_query(self, query, params=None):
		if params is None:
			self.cursor.execute(query)
		else:
			self.cursor.execute(query, params)
		return self.cursor.fetchone()

	def get_description(self):
		column_names = [description[0] for description in self.cursor.description]
		return column_names
