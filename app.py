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
<footer>Romo Alvarado Luis Angel 23308060610320
</footer>
    '''
    return(mensaje)
    
    
@app.route('/sumar/<v1>/<v2>')
def Suma(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    Sum= num1+num2
    return(f"La suma de {v1} y {v2} es: {Sum}")

@app.route('/restar/<v1>/<v2>')
def Restar(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    res= num1-num2
    return(f"La resta de {v1} y {v2} es:{res}")

@app.route('/dividir/<v1>/<v2>')
def division(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    div= num1/num2
    return(f"La division de {v1} y {v2} es: {div}")

@app.route('/multiplicar/<v1>/<v2>')
def multiplicacion(v1, v2):
    num1 = int(v1)
    num2 = int(v2)
    mul= num1*num2
    return(f"La multiplicacion de {v1} y {v2} es: {mul}")
    


if __name__ == '__main__':
    app.run(debug=True)