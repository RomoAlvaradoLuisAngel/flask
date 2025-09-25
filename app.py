from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hola_mundo():
    return '<h1>Hola mundo desde Flask!</h1>'

@app.route('/otra')
def Hola_mundo1():
    return '<h1>Hola mundo desde otra ruta!</h1>'

if __name__ == '__main__':
    app.run(debug=True)