from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_bcrypt import Bcrypt
from connection import obtener_conexion
import datetime
import models

# Modelo de Vista-Controlador -------------------------------------------------.
#Instancia de app.
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'myapp123'

#Inicio de Sesión -------------------------------------------------------------.

# Identificar Rutas ------------------------------------------------------------.
# Ruta Inicio.
@app.route("/inicio")
@app.route("/")
def home():
    if 'user' in session:
        a = 'Activa'
        return render_template("/index.html", ms = a)
    else:
        a = 'Terminada'
        return render_template("/index.html", userSession = session, ms = a)

@app.route("/ayuda")
def help():
    return render_template("/help.html")

@app.route("/contacto")
def contact():
    return render_template("/contact.html")

#Inicio, Registro de Sesión -----------------------------------------------------
@app.route("/acceso")
def login():
    return render_template("/login.html")

loginIndex = -1
cualUsuario = 0

@app.route("/verificar", methods=["POST"])
def check():
    global loginIndex, cualUsuario
    if request.method == "POST":
        checkIn = models.registros_emp()
        email = request.form['email']
        password = request.form['password']
        print(checkIn)
        signed = False
        i = 0
        for checks in checkIn:
            if email == checks[7] and password == checks[6]:
                loginIndex = i
                session['user'] = checks[1]
                cualUsuario = checks[0]
                print(checks)
                print(cualUsuario)
                signed = True
            i += 1
        if not signed:
            flash('Correo/Contraseña Incorrecta!')
            return redirect(url_for('login'))
        
        flash('Bienvenido ' + checkIn[loginIndex][1] + ' ' + checkIn[loginIndex][2] + ' !')
        return redirect(url_for('home'))
    else:
        return 'Bad Request'

@app.route("/terminar")
def logout():
    global loginIndex
    session.clear()
    checkIn = models.registros_emp()
    flash('Hasta luego ' + checkIn[loginIndex][1] + ' ' + checkIn[loginIndex][2] + ' !')
    return redirect(url_for('home'))

@app.route("/registro")
def register():
    return render_template("/register.html")

#Pestañas de consulta a BD ------------------------------------------------------.
@app.route("/empleados")
def employees():
    empleado = models.registros_emp()
    tx = 'Empleados'
    return render_template("/types/employee.html", valores = empleado, type = tx)

@app.route("/productos")
def product():
    producto = models.registros_prod()
    tx = 'Producto'
    return render_template("/types/product.html", valores = producto, type = tx)

@app.route("/categoria")
def category():
    categoria = models.registros_cat()
    tx = 'Categoria'
    return render_template("/types/category.html", valores = categoria, type = tx)

@app.route("/proveedor")
def supplier():
    proveedor = models.registros_prov()
    tx = 'Proveedor'
    return render_template("/types/supplier.html", valores = proveedor, type = tx)

@app.route("/clientes")
def client():
    cliente = models.registros_cli()
    tx = 'Cliente'
    return render_template("/types/client.html", valores = cliente, type = tx)

#Sistema de ventas ------------------------------------------------------------.
ventaMsg = 'Venta'
item = 0
canasta = []
data1 = []
totalPago = 0.0
registros = ''
    #Fecha -----
x = datetime.datetime.now()
dateNow = str(x.strftime('%x'))
dateNow.replace('/','-')
print(dateNow)
    #------------
print(cualUsuario)

@app.route("/venta")
def sale():
    global ventaMsg
    return render_template("/types/sale.html", datos = canasta, tp = totalPago, type = ventaMsg)

@app.route("/busqCanasta", methods=['GET', 'POST'])
def searchData():
    global ventaMsg, canasta, cualUsuario, registros, data1, item, totalPago
    valorTamFactura = models.tam_fact()
    registros = '100000' + str(valorTamFactura[0][0] + 1)
    if request.method == 'POST':
        if int(request.form['accion']) == 1:
            code = request.form['codCli']
            data1 = models.buscar_reg_cli(code)
            if len(data1) == 0:
                print('No existe registro')
                data1 = [[0, 'x', 'y']]
                return render_template("/types/sale.html", numFact = registros, inf1 = data1[0], datos = canasta, tp = totalPago, type = ventaMsg)
            return render_template("/types/sale.html", numFact = registros, inf1 = data1[0], datos = canasta, tp = totalPago, type = ventaMsg)
        if int(request.form['accion']) == 2:
            code = request.form['codProd']
            data2 = models.buscar_reg_prod(code)
            if len(data2) == 0:
                print('No existe registro')
                data2 = [[0, 'x', 'y', 'z']]
                return render_template("/types/sale.html", numFact = registros, inf1 = data1[0],  inf2 = data2[0], datos = canasta, tp = totalPago, type = ventaMsg)
            return render_template("/types/sale.html", numFact = registros, inf1 = data1[0], inf2 = data2[0], datos = canasta, tp = totalPago, type = ventaMsg)
        if int(request.form['accion']) == 3:
            item += item
            code = request.form['codigo']
            desc = request.form['infoProd']
            print(request.form['precio'])
            prace = float(request.form['precio'])
            cant = int(request.form['cantidad'])
            subt = prace * cant
            
            lista = [item, code, desc, prace, cant, subt]
            print(lista)
            diccionario = {}
            diccionario[lista[1]] = 1
            i = 0
            for productoLista in canasta:
                diccionario [productoLista[1]] = diccionario.get(productoLista[1],0)+1
                if diccionario[productoLista[1]] >= 2:
                    lista[4] += productoLista[4]
                    canasta.pop(i)
                    break
                i += 1
            canasta.append(lista)
            i = 0
            while i < len(canasta):
                canasta[i][0] = i + 1
                i += 1
            print(canasta)
            
            totalPago = 0
            for articulo in canasta:
                totalPago += articulo[5]
            
            return render_template("/types/sale.html", numFact = registros, inf1 = data1[0], tp = totalPago,  datos = canasta, type = ventaMsg)

@app.route("/terminarVenta")
def cashout():
    global canasta, cualUsuario, registros, data1, totalPago
    for articulo in canasta:
        cantidad = articulo[4]
        idproducto = int(articulo[1])
        rs = models.buscar_reg_prod(idproducto)
        stockAct = int(rs[0][5]) - int(cantidad)
        models.actualizarStock(idproducto, stockAct)
        
    df1 = data1[0][0] #Id del cliente
    df2 = cualUsuario #Id del empleado
    df3 = registros #Numero de Factura
    df4 = dateNow #Fecha
    df5 = totalPago #Total de pago
    df6 = 1 #Factura valida
    print(df1, df2, df3, df4, df5, df6)
    models.insertar_reg_fact(df4, df3, df2, df1, df5, df6)
    print(canasta)
    numVenta = models.buscar_fact()
    for articulo in canasta:
        r1 = numVenta[0][0]
        reg2 = models.buscar_prod_nombre(articulo[2])
        r2 = reg2[0][0]
        r3 = articulo[4]
        r4 = articulo[5]
        print(r1, r2, r3, r4)
        models.insertar_reg_detalle(r1, r2, r3, r4)
    canasta = []
    totalPago = 0
    return render_template("/types/sale.html", datos = canasta, tp = totalPago, type = ventaMsg)
            
@app.route("/factura")
def invoice():
    tx = 'Facturas'
    reg = models.registros_facts()
    return render_template("/types/invoice.html", type = tx, valores = reg)

#Formularios de Registro -------------------------------------------------------.
@app.route("/formAddEmpleados")
def form_emp():
    tx = 'Empleados'
    return render_template("/forms/form_emp.html", type = tx)

@app.route("/formAddProducto")
def form_prod():
    tx = 'Producto'
    detalle1 = models.registros_cat()
    detalle2 = models.registros_prov()
    return render_template("/forms/form_prod.html", type = tx, exp1 = detalle1, exp2 = detalle2)

@app.route("/formAddCategoria")
def form_cat():
    tx = 'Categoria'
    return render_template("/forms/form_cat.html", type = tx)

@app.route("/formAddProveedor")
def form_prov():
    tx = 'Proveedor'
    return render_template("/forms/form_prov.html", type = tx)

@app.route("/formAddCliente")
def form_cli():
    tx = 'Cliente'
    return render_template("/forms/form_cli.html", type = tx)

#Formulario de Actualizar Registro ----------------------------------------------.
@app.route("/formEditEmpleados/<string:id>")
def form_emp_edit(id):
    empleado = models.buscar_reg_emp(id)
    tx = 'Empleados'
    return render_template("/forms/form_emp_edit.html", empleado = empleado[0], type = tx)

@app.route("/formEditProducto/<string:id>")
def form_prod_edit(id):
    producto = models.buscar_reg_prod(id)
    detalle1 = models.registros_cat()
    detalle2 = models.registros_prov()
    tx = 'Producto'
    return render_template("/forms/form_prod_edit.html", producto = producto[0], type = tx, exp1 = detalle1, exp2 = detalle2)

@app.route("/formEditCategoria/<string:id>")
def form_cat_edit(id):
    categoria = models.buscar_reg_cat(id)
    tx = 'Categoria'
    return render_template("/forms/form_cat_edit.html", categoria = categoria[0], type = tx)

@app.route("/formEditProveedor/<string:id>")
def form_prov_edit(id):
    proveedor = models.buscar_reg_prov(id)
    tx = 'Proveedor'
    return render_template("/forms/form_prov_edit.html", proveedor = proveedor[0], type = tx)

@app.route("/formEditCliente/<string:id>")
def form_cli_edit(id):
    cliente = models.buscar_reg_cli(id)
    tx = 'Cliente'
    return render_template("/forms/form_cli_edit.html", cliente = cliente[0], type = tx)

#Acciones de operación ----------------------------------------------------------.
# --> Agregar
@app.route("/agregarEmployee", methods=['POST'])
def addEmployee():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        estado = request.form['estado']
        tel = request.form['tel']
        password = request.form['password']
        email = request.form['email']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.insertar_reg_emp(nombre, apellido, edad, estado, tel, password, email)
        return redirect(url_for('employees'))

@app.route("/agregarProduct", methods=['POST'])
def addProduct():
    if request.method == 'POST':
        categoria = request.form['categoria']
        proveedor = request.form['proveedor']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        existencia = request.form['existencia']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.insertar_reg_prod(categoria, proveedor, nombre, precio, cantidad, existencia)
        return redirect(url_for('product'))
    
@app.route("/agregarCategory", methods=['POST'])
def addCategory():
    if request.method == 'POST':
        nombre = request.form['nombre']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.insertar_reg_cat(nombre)
        return redirect(url_for('category'))
    
@app.route("/agregarProveedor", methods=['POST'])
def addSupplier():
    if request.method == 'POST':
        nombre = request.form['nombre']
        dni = request.form['dni']
        nac = request.form['nac']
        tel = request.form['tel']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.insertar_reg_prov(nombre, dni, nac, tel)
        return redirect(url_for('supplier'))
    
@app.route("/agregarClient", methods=['POST'])
def addClient():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        estado = request.form['estado']
        tel = request.form['tel']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.insertar_reg_cli(nombre, apellido, estado, tel)
        return redirect(url_for('client'))

# --> Actualizar -------------------------------------------------------------------.
@app.route("/actualizarEmpleados/<string:id>", methods=['POST'])
def editEmployee(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        estado = request.form['estado']
        tel = request.form['tel']
        password = request.form['password']
        email = request.form['email']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.actualizar_reg_emp(id, nombre, apellido, edad, estado, tel, password, email)
        return redirect(url_for('employees'))

@app.route("/actualizarProducto/<string:id>", methods=['POST'])
def editProduct(id):
    if request.method == 'POST':
        categoria = request.form['categoria']
        proveedor = request.form['proveedor']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        existencia = request.form['existencia']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.actualizar_reg_prod(id, categoria, proveedor, nombre, precio, cantidad, existencia)
        return redirect(url_for('product'))

@app.route("/actualizarCategoria/<string:id>", methods=['POST'])
def editCategory(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.actualizar_reg_cat(id, nombre)
        return redirect(url_for('category'))

@app.route("/actualizarProveedor/<string:id>", methods=['POST'])
def editSupplier(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        dni = request.form['dni']
        nac = request.form['nac']
        tel = request.form['tel']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.actualizar_reg_prov(id, nombre, dni, nac, tel)
        return redirect(url_for('supplier'))
    
@app.route("/actualizarCliente/<string:id>", methods=['POST'])
def editCliente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        estado = request.form['estado']
        tel = request.form['tel']
        #print(nombre, apellido, edad, estado, tel, password, email)
        models.actualizar_reg_cli(id, nombre, apellido, estado, tel)
        return redirect(url_for('client'))
    
# --> Eliminar ---------------------------------------------------------------------
@app.route("/eliminarEmpleados/<string:id>")
def deleteEmp(id):
    models.eliminar_reg_emp(id)
    return redirect(url_for("employees"))

@app.route("/eliminarProducto/<string:id>")
def deleteProd(id):
    models.eliminar_reg_prod(id)
    return redirect(url_for("product"))

@app.route("/eliminarCategoria/<string:id>")
def deleteCat(id):
    models.eliminar_reg_cat(id)
    return redirect(url_for("category"))

@app.route("/eliminarProveedor/<string:id>")
def deleteProv(id):
    models.eliminar_reg_prov(id)
    return redirect(url_for("supplier"))

@app.route("/eliminarCliente/<string:id>")
def deleteCli(id):
    models.eliminar_reg_cli(id)
    return redirect(url_for("client"))

#Arranque de App con Debugger ------------------------------------------------------.
if __name__ == "__main__":
    app.run(debug=True)