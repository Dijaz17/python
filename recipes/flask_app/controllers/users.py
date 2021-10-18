from flask import render_template, request, redirect, session
from flask.helpers import flash

from flask_app.models.user import User

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_account', methods=['POST'])
def create_acc():
    if not User.validate_registration(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    User.save(data)

    new_user = User.get_indiv_by_email(data)
    session['id'] = new_user[0].id
    session['first_name'] = new_user[0].first_name
    session['last_name'] = new_user[0].last_name
    session['email'] = new_user[0].email

    return redirect('/logged_in')

@app.route('/login', methods=['POST'])
def log_in():
    user_exists = False
    data = {
        'email': request.form['email']
    }
    if len(User.get_indiv_by_email(data)) > 0:
        user_exists = True
        existing_user = User.get_indiv_by_email(data)
    if not user_exists:
        flash('Email is not associated with an account')
        return redirect('/')
    if not bcrypt.check_password_hash(existing_user[0].password, request.form['password']):
        flash('Incorrect password')
        return redirect('/')

    session['id'] = existing_user[0].id
    session['first_name'] = existing_user[0].first_name
    session['last_name'] = existing_user[0].last_name
    session['email'] = existing_user[0].email
    return redirect('/logged_in')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out')

    return redirect('/')

@app.route('/logged_in')
def logged_in():
    if 'id' not in session:
        return redirect('/')
    return redirect('/recipes')