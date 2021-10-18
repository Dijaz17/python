from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'asdfjkl'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def display_results():
    return render_template('/results.html', name = session['name'], dojoLocation = session['dojoLocation'], favLang = session['favLang'], comment = session['comment'])

if(__name__ == "__main__"):
    app.run(debug = True)