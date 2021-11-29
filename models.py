from connection import obtener_conexion

#Consultas extraordinarias.

#Consultas de Base de Datos

#Consultas de ventas.
def tam_fact():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT count('') FROM factura")
    reg = cur.fetchall()
    return reg

def buscar_fact():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT max(id_factura) FROM factura")
    reg = cur.fetchall()
    return reg

def insertar_reg_fact(a, b, c, d, e, f):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into factura (fecha, serie, empleado, cliente, monto, existencia) values (?, ?, ?, ?, ?, ?)", (a, int(b), c, d, e, f))
    conexion.commit()

def insertar_reg_detalle(a, b, c, d):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into detalleVenta (factura, producto, cantidad, precioVenta) values (?, ?, ?, ?)", (a, b, c, d))
    conexion.commit()

def buscar_prod_nombre(n):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM producto WHERE nombre = ?", n)
    reg = cur.fetchall()
    return reg

def actualizarStock(i, a):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE producto set cantidad = ? where id_producto = {0}".format(i), (a))
    conexion.commit()

#Consultas de registros.
def registros_emp():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM empleado")
    reg = cur.fetchall()
    return reg

def registros_prod():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM producto")
    reg = cur.fetchall()
    return reg

def registros_cat():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM categoria")
    reg = cur.fetchall()
    return reg

def registros_prov():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM proveedor")
    reg = cur.fetchall()
    return reg

def registros_cli():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM cliente")
    reg = cur.fetchall()
    return reg
'''
#Consultas Extras - Foraneas.
def registros_cat_ext():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM categoria where categoria.id_categoria")
    reg = cur.fetchall()
    return reg

def registros_prov_ext():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM proveedor where proveedor.id_proveedor")
    reg = cur.fetchall()
    return reg
'''
#Alta de registros.
def insertar_reg_emp(a, b, c, d, e, f, g):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into empleado (nombre, apellido_p, edad, estado, telefono, pass, email) values (?, ?, ?, ?, ?, ?, ?)", (a, b, c, d, e, f, g))
    conexion.commit()
    
def insertar_reg_prod(a, b, c, d, e, f):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into producto (categoria, proveedor, nombre, precio, cantidad, existencia) values (?, ?, ?, ?, ?, ?)", (a, b, c, float(d), e, f))
    conexion.commit()
    
def insertar_reg_cat(a):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into categoria (nombre) values (?)", (a))
    conexion.commit()
    
def insertar_reg_prov(a, b, c, d):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into proveedor (nombre, dni, nacionalidad, telefono) values (?, ?, ?, ?)", (a, b, c, d))
    conexion.commit()

def insertar_reg_cli(a, b, c, d):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("INSERT into cliente (nombre, apellido_p, estado, telefono) values (?, ?, ?, ?)", (a, b, c, d))
    conexion.commit()
    
#Actualización de Registros.
def actualizar_reg_emp(i, a, b, c, d, e, f, g):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE empleado set nombre = ?, apellido_p = ?, edad = ?, estado = ?, telefono = ?, pass = ?, email = ? where id_empleado = {0}".format(i), (a, b, c, d, e, f, g))
    conexion.commit()
    
def actualizar_reg_prod(i, a, b, c, d, e, f):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE producto set categoria = ?, proveedor = ?, nombre = ?, precio = ?, cantidad = ?, existencia = ? where id_producto = {0}".format(i), (a, b, c, float(d), e, f))
    conexion.commit()

def actualizar_reg_cat(i, a):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE categoria set nombre = ? where id_categoria = {0}".format(i), (a))
    conexion.commit()

def actualizar_reg_prov(i, a, b, c, d):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE proveedor set nombre = ?, dni = ?, nacionalidad = ?, telefono = ? where id_proveedor = {0}".format(i), (a, b, c, d))
    conexion.commit()
    
def actualizar_reg_cli(i, a, b, c, d):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("UPDATE cliente set nombre = ?, apellido_p = ?, estado = ?, telefono = ? where id_cliente = {0}".format(i), (a, b, c, d))
    conexion.commit()

#Buscar registro registros.
def buscar_reg_emp(x):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM empleado WHERE id_empleado = {0}".format(x))
    reg = cur.fetchall()
    return reg

def buscar_reg_prod(x):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM producto WHERE id_producto = {0}".format(x))
    reg = cur.fetchall()
    return reg

def buscar_reg_cat(x):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM categoria WHERE id_categoria = {0}".format(x))
    reg = cur.fetchall()
    return reg

def buscar_reg_prov(x):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM proveedor WHERE id_proveedor = {0}".format(x))
    reg = cur.fetchall()
    return reg

def buscar_reg_cli(x):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM cliente WHERE id_cliente = {0}".format(x))
    reg = cur.fetchall()
    return reg

#Baja de registros.
def eliminar_reg_emp(y):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("DELETE FROM empleado WHERE id_empleado = {0}".format(y))
    conexion.commit()
    
def eliminar_reg_prod(y):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("DELETE FROM producto WHERE id_producto = {0}".format(y))
    conexion.commit()
    
def eliminar_reg_cat(y):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("DELETE FROM categoria WHERE id_categoria = {0}".format(y))
    conexion.commit()
    
def eliminar_reg_prov(y):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("DELETE FROM proveedor WHERE id_proveedor = {0}".format(y))
    conexion.commit()

def eliminar_reg_cli(y):
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("DELETE FROM cliente WHERE id_cliente = {0}".format(y))
    conexion.commit()
