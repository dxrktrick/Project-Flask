from connection import obtener_conexion

def obtener_reg():
    conexion = obtener_conexion()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM Producto")
    reg = cur.fetchall()
    conexion.close()
    return reg