from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = '''
    <h1>bienvenidos a la calculadora de Python</h1>
<p>1.- para sumar escribe en el navegador 127.0.0.1:5000/sumar/10/20</p>
<p>2.- para restar escribe en el navegador 127.0.0.1:5000/restar/10/20</p>
<p>3.- para dividir escribe en el navegador 127.0.0.1:5000/dividir/10/20</p>
<p>4.- para multiplicar escribe en el navegador 127.0.0.1:5000/multiplicar/10/20</p>
    '''
    
app.route('/sumar')
def Suma(v1):
    val1=10
    val2=20
    Sum=val1+val2
    
    return("La suma de " + val1 " y " + val2 " es: " + Sum)
    


if __name__ == '__main__':
    app.run(debug=True)