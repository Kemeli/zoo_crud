from Tables import Data_base

def delete_animal(id):
    db = Data_base('database.db')
    db.connect()
    query = "DELETE FROM Animais WHERE ID_Animal = (?)"
    db.execute_query(query, (id,))
    db.close()


def delete_specie(id_specie):
    db = Data_base('database.db')
    db.connect()
    query = "SELECT * FROM Animais WHERE ID_Especie = (?)"
    animal = db.fetch_one_query(query, (id_specie,))
    if animal:
        print ("Selected specie is not empty")
    else:
        query = "DELETE FROM Especies WHERE ID_Especie = (?)"
        db.execute_query(query, (id_specie,))
    db.close()
