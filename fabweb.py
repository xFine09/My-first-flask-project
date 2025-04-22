import sys
from flask import Flask
from fab import tanper

app = Flask(__name__)
@app.route('/')
def pintafab():
    tanteo = open(sys.argv[1], 'r')
    parciales, teams = tanper(tanteo)
    salida = ''
    for cuarto, parcial in parciales.items():
        salida +='{}º Cuarto.&emsp;'.format(cuarto)
        for equipo, puntos in parcial.items():
            salida += '{}:{}&emsp;'.format(teams[equipo], puntos)
        salida+= '<br>'
    tanteo.close()
    return salida
        
if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug=True) 