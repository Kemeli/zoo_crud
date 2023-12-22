import sqlite3
from datetime import date

def get_db_connection():
	connection = sqlite3.connect('database.db')
	return connection


def add_specie_to_table(specie):
	db = get_db_connection()
	cursor = db.cursor()
	query = "INSERT INTO Especies (Nome_Cientifico) VALUES (?)"
	cursor.execute(query, (specie,))
	db.commit()
	db.close()


def add_animal_to_table(animal, name, age, specie):
	#no front a o select para escolher a especie do animal deve ser obrigatório
	if specie == None:
		print("passar a espécie")
		return

	data_atual = date.today()

	db = get_db_connection()
	cursor = db.cursor()

	query = "SELECT ID_Especie FROM Especies WHERE Nome_Cientifico = (?)"
	cursor.execute(query, (specie,)) #depois colocar um select com os nomes disponiveis, pegando direto do db
	#talvez aqui checar se os dados passados não existem na tabela e caso sim, confirmar a adição
	id_specie = cursor.fetchone()[0]

	query = "INSERT INTO Animais (Nome, Animal, Idade, ID_Especie, Data_Entrada) VALUES (?, ?, ?, ?, ?)"
	db.execute(query, (name, animal, age, id_specie, data_atual))
	db.commit()
	db.close()
	return True



def print_animal():
	db = get_db_connection()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM Animais")
	# cursor.execute("SELECT * FROM animals WHERE animal = ?", (animal,))

	# item = cursor.fetchone()
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	db.close()
