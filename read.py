from Tables import Data_base

# def get_db_connection():
# 	connection = sqlite3.connect('database.db')
# 	return connection


# def add_specie_to_table(specie):
# 	db = get_db_connection()
# 	cursor = db.cursor()
# 	query = "INSERT INTO Especies (Nome_Cientifico) VALUES (?)"
# 	cursor.execute(query, (specie,))
# 	db.commit()
# 	db.close()


# def add_animal_to_table(animal, name, age, specie):
# 	#no front a o select para escolher a especie do animal deve ser obrigatório
# 	if specie == None:
# 		print("passar a espécie")
# 		return

# 	data_atual = date.today()

# 	db = get_db_connection()
# 	cursor = db.cursor()

# 	query = "SELECT ID_Especie FROM Especies WHERE Nome_Cientifico = (?)"
# 	cursor.execute(query, (specie,)) #depois colocar um select com os nomes disponiveis, pegando direto do db
# 	#talvez aqui checar se os dados passados não existem na tabela e caso sim, confirmar a adição
# 	id_specie = cursor.fetchone()[0]

# 	query = "INSERT INTO Animais (Nome, Animal, Idade, ID_Especie, Data_Entrada) VALUES (?, ?, ?, ?, ?)"
# 	db.execute(query, (name, animal, age, id_specie, data_atual))
# 	db.commit()
# 	db.close()
# 	return True

def get_all_species():
	db = Data_base('database.db')
	db.connect()
	rows = db.fetch_query("SELECT * FROM Especies")
	db.close()
	return rows

def get_all_animals():
	db = Data_base('database.db')
	db.connect()
	rows = db.fetch_query("SELECT * FROM Animais")
	db.close()
	return rows

def get_animals_table():
	db = Data_base('database.db')
	db.connect()
	rows = db.fetch_query("SELECT * FROM Animais")
	columns_names = [description[0] for description in db.cursor.description]
	rows.insert(0, columns_names)
	db.close()
	return rows

def get_age_average():
	db = Data_base('database.db')
	db.connect()
	avg_age = db.fetch_one_query("SELECT AVG(Idade) FROM Animais", None)
	print (avg_age)


#pegar por um select, onde vai ter a espécie, o ID e a descrição
#ai nem precisa consultar a tabela,só passar o ID para a tabela e buscar os animais
# def get_animals_by_specie(id_especie):
#	 db = Data_base('database.db')
#	 db.connect()
#	 query = "SELECT * FROM Animais WHERE ID_Especie = (?)"
#	 rows = db.fetch_query(query, (id_especie,))
#	 db.close()
#	 for row in rows:
#		 print(row)


def get_row_item(id, table, key_word):
	db = Data_base('database.db')
	db.connect()
	query = f"SELECT * FROM {table} WHERE {key_word} = (?)"
	item = db.fetch_one_query(query, (id,))
	db.close()
	return (item)

def get_animals_by_query(key_value, column):
	db = Data_base('database.db')
	db.connect()
	query = f"SELECT * FROM Animais WHERE {column} = (?)"
	itens = db.fetch_query(query, (key_value,))
	return itens

#a informação se é maior, menor ou igual, deve vir do front
def get_animals_by_age(operator, value):
	db = Data_base('database.db')
	db.connect()
	query = f"SELECT * FROM Animais WHERE Idade {operator} (?)"
	itens = db.fetch_query(query, (value,))
	return itens

def get_animals_by_specie(specie):
	itens = get_animals_by_query(specie, "ID_Especie")
	return itens
