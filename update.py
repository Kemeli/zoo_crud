from Tables import Data_base

def update_info(new_info, id, table, column, row):
    db = Data_base('database.db')
    db.connect()
    query = f"UPDATE {table} SET {column} = (?) WHERE {row} = (?)"
    db.execute_query(query, (new_info, id,))
    db.close()


def update_animal_name(id_value, new_name):
    update_info(new_name, id_value, "Animais", "Nome", "ID_Animal")


#considerando que a pessoa vai ter que escolher uma especie existente no front
def update_animal_specie(new_specie, id_value):
    update_info(new_specie, id_value, "Animais", "Especie", "ID_Animal")


def update_animal_type(new_type, id_value):
    update_info(new_type, id_value, "Animais", "Animal", "ID_Animal")


def update_specie_description(new_description, id_value):
    update_info(new_description, id_value, "Especies", "Descricao", "ID_Especie")


def update_specie_description(new_specie, id_value):
    update_info(new_specie, id_value, "Especies", "Nome_Cientifico", "ID_Especie")


def update_animals_age(id_animal, new_age):
    db = Data_base('database.db')
    db.connect()
    query = "SELECT Idade FROM Animais WHERE ID_Animal = (?)"
    age = db.fetch_one_query(query, (id_animal,))
    if age[0] > new_age:
        db.close()
        return "invalid animal age update"
    query = "UPDATE Animais SET Idade = (?) WHERE ID_Animal = (?)"
    db.execute_query(query, (new_age, id_animal,))
    db.close()
    return None
