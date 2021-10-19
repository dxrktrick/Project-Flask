from flask import Flask, render_template
import controller

#Aplicación
app = Flask(__name__)

# Modelo de Vista-Controlador.
# Identificar Rutas.

@app.route("/")
def index():
    return render_template("/index.html", User = 'Anonymous')

@app.route("/consultarProd")
def registros():
    pdts = controller.obtener_reg()
    return render_template("/consultarProductos.html",
                text = 'Registros Completos',
                registros = pdts)

app.run()

# | Vázquez D. J. Eric.
# | Carreola A. Gustavo.
# | Sistemas Gestores De Bases De Datos.

#Actualizar entorno de aplicación
#venv\Scripts\activate
#set FLASK_APP=app
#FLASK run