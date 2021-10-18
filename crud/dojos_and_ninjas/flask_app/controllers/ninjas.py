from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

from flask_app import app

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def homepage():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)

@app.route('/dojo/new', methods=['POST'])
def newDojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_indiv(id)
    ninjas = Ninja.get_all_from_dojo(id)
    return render_template('showDojo.html', ninjas = ninjas, dojo=dojo)

@app.route('/ninjas')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template('createNinja.html', dojos = dojos)

@app.route('/new_ninja', methods=['POST'])
def add_ninjas():
    data = {
        "fname": request.form["fname"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    id_dojo = request.form["dojo_id"]
    return redirect(f'/dojos/{id_dojo}')
