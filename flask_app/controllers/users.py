from flask import render_template, request, redirect

from flask_app.models.user import User

from flask_app import app

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', all_users = users)

@app.route('/create_user')
def create_user():
    return render_template('user_cr.html')

@app.route('/users/new', methods=['POST'])
def create_new_user():
    data = {
        "fname": request.form["fname"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users/redirect')

@app.route('/users/redirect')
def redirect_to_show():
    users = User.get_all()
    user = users[len(users)-1] 
    return redirect(f'/users/{user.id}')

@app.route('/users/<int:id>')
def show_user(id):
    user = User.get_indiv(id)
    return render_template('individual_user.html', user = user)

@app.route('/users/<int:id>/edit')
def user_editor(id):
    user = User.get_indiv(id)
    return render_template('user_edit.html', user=user)

@app.route('/editing_user/<int:id>', methods=['POST'])
def update_user(id):
    data = {
        "fname": request.form["fname"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(data, id)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/destroy')
def destroy_user(id):
    User.destroy(id)
    return redirect('/')
