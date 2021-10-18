from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html', row = 8, column = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:column>')
def checkerboardRow(column):
    return render_template('checkerboard.html', row = 8, column = column, color1 = 'red', color2 = 'black')

@app.route('/<int:column>/<int:row>')
def checkerboardRowCol(column, row):
    return render_template('checkerboard.html', row = row, column = column, color1 = 'red', color2 = 'black')

@app.route('/<int:column>/<int:row>/<color1>/<color2>')
def checkerboardCustom(column, row, color1, color2):
    return render_template('checkerboard.html', row = row, column = column, color1 = color1, color2 = color2)

if(__name__ == "__main__"):
    app.run(debug = True)