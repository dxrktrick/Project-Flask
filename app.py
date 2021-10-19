from flask import Flask, render_template
import controller

#Aplicación
app = Flask(__name__)

# Modelo de Vista-Controlador.
# Identificar Rutas.

@app.route("/")
def hello_world():
    return render_template("/index.html", User = 'Anonymous')

@app.route("/")
def registros():
    pdts = controller.obtener_reg()
    return render_template("/consultaProductos.html",
                text = 'Registros Completos',
                registros = pdts)

app.run()

# | Vázquez D. J. Eric.
# | Carreola A. Gustavo.
# | Sistemas Gestores De Bases De Datos