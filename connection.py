import pyodbc

def obtener_conexion():
    try:
        return pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-PF9ESBE3;DATABASE=WikiPartners;UID=sa;PWD=Michis24')
    except Exception as ex:
        return print("ex")