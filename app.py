from read import *
from create import *
from update import *
from Tables import *
from Animal import Animal
from flask import Flask, jsonify, render_template, request
# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/adicionar_animal", methods=['GET', 'POST'])
def new_animal():
	if request.method == 'POST':
		age = request.form['age']
		name = request.form['name']
		animal_type = request.form['animal_type']
		specie = request.form['species']
		add_animal(animal_type, age, name, specie)
	species = get_all_species()
	species_name = [specie[1] for specie in species]
	return render_template("add_animal.html", species_list=species_name)


@app.route("/adicionar_especie", methods=['GET', 'POST'])
def new_specie():
	if request.method == 'POST':
		specie = request.form['specie']
		description = request.form['description']
		add_species(specie, description)
	return render_template("add_specie.html")

#pegar o animal pelo id e ver os campos que foram preenchidos
@app.route("/atualizar_animal", methods=['GET', 'POST'])
def update_animal():
	if request.method == 'POST':
		message = ''
		animal = request.form["animal"]
		print(animal)
		print('id', animal[1])
		name = request.form['name']
		age = request.form['age']
		print(age)
		animal_type = request.form['animal_type']
		id = animal[1]
		if name:
			update_animal_name(id, name)
		if age:
			print(id, age)
			message = update_animals_age(id, age)
		if animal_type:
			update_animal_type(id, animal_type)
		if message:
			return render_template("update_animal.html", animal_list=rows, message=message)
	rows = get_all_animals()
	# animals = [animal[1] for animal in rows]
	return render_template("update_animal.html", animal_list=rows)


@app.route('/get_animals', methods=['GET'])
def get_animals():
	data = get_animals_table()
	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)

# if __name__ == "__main__":
	# go()
	# get_animals_by_specie(2)
	# update_animals_age(2, 3)
	# item = get_row_item(2, "Animais", "ID_Animal")
	# print(item)
	# delete_animal(1)
	# delete_specie(2)
	# update_specie_description("animal que mama", 2)
	# update_animal_type("cobra", 6)
	# update_animal_name(6, "sneiq")
	# itens = get_animals_by_age(">", "Animais", 1)
	# for item in itens:
		# print (item)
	# add_species("mamifero", "mama")
	# add_species("peixe", "nada")
	# add_species("anfíbio", "molhado")
	# add_animal("leão", 3, "junior", "mamifero")
	# add_animal("sapo", 2, "bob", "anfibio")
	# add_animal("cobra", 2, "Ala", "anfibo")

	# age_avg = get_age_average()
