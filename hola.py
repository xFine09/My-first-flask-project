from flask import Flask
app = Flask(__name__)
@app.route('/')
def pintahola():
    return ('<h1>Hola Mundo!</h1>')
@app.route('/alumnos/')
def alumnos():
    return ('<h1>Alumno</h1>')
@app.route('/empresa/')
def empresa():
    return ('<h1>Empresa</h1>')

@app.route('/saluda/<nombre>')
def saluda(nombre):
    return ('<h1>Hola: {}</h1>'.format(nombre))

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug=True) 