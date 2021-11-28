import pyodbc
#Session - Gus (1), Eric (2)

value = 1

def obtener_conexion():
    if value == 1:
        try:
            connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=DXRKLIGHT;DATABASE=WikiPartners;Trusted_Connection=yes;')
            print('Conexion exitosa')
            return connection
        except Exception as ex:
            return print(ex)
    elif value == 2:
        try:
            connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-PF9ESBE3;DATABASE=WikiPartners;Trusted_Connection=yes;')
            print('Conexion exitosa')
            return connection
        except Exception as ex:
            return print(ex)
