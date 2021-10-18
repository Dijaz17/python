from flask import render_template, request, redirect, session
from flask.helpers import flash

from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_app import app

@app.route('/recipes')
def recipes_index():
    if 'id' not in session:
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    return render_template('recipes_index.html', all_recipes = recipes)

@app.route('/create_recipe')
def create_recipe():
    if 'id' not in session:
        return redirect('/')
    return render_template('create_recipe.html')

@app.route('/creating_recipe', methods=['POST'])
def creating_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes')
    
    data = {
        'name': request.form['name'],
        'under_thirty': request.form['under_thirty'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id': request.form['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')

@app.route('/show_recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    for recipe in recipes:
        if recipe.id == recipe_id:
            correct_recipe = recipe
    return render_template('show_recipe.html', recipe = correct_recipe)

@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    recipes = Recipe.get_all_recipes()
    for recipe in recipes:
        if recipe.id == recipe_id:
            correct_recipe = recipe

    if session['id'] != correct_recipe.user_id:
        return redirect('/recipes')
    return render_template('edit_recipe.html', recipe = correct_recipe)

@app.route('/editing_recipe', methods=['POST'])
def editing_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes')
    
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'under_thirty': request.form['under_thirty'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id': request.form['user_id']
    }
    Recipe.update_recipe(data)
    return redirect('/recipes')

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
        
    recipes = Recipe.get_all_recipes()
    for recipe in recipes:
        if recipe.id == recipe_id:
            correct_recipe = recipe
    if session['id'] != correct_recipe.user_id:
        return redirect('/recipes')
    
    Recipe.delete(recipe_id)
    return redirect('/recipes')
