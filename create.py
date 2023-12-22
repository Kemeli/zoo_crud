from Tables import Data_base
from Animal import Animal
from datetime import date

#tem q verificar se a especie existe antes
def add_species(specie, description):
    db = Data_base('database.db')
    db.connect()
    query = "INSERT INTO Especies (Especie, Descricao) VALUES (?, ?)"
    params = (specie, description)
    db.execute_query(query, params)
    db.close()

#verificar se a especie ja não existe
def add_animal(animal, age, name, specie):
    curr_date = date.today()
    db = Data_base('database.db')
    db.connect()
    animal = Animal(animal, name, age, specie)
    query = "INSERT INTO Animais (Animal, Nome, Idade, Especie, Data_Entrada) VALUES (?, ?, ?, ?, ?)"
    params = (animal.animal, animal.name, animal.age, animal.specie, curr_date)
    db.execute_query(query, params)
    db.close()
