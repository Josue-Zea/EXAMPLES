from flask import jsonify
from mysql.connector import connect, Error

myHost = "localhost"
myUser="root"
myPassword="my-secret-pw"
myDatabase="PRUEBAS"

def createConnection():
    try:
        return connect(
            host=myHost,
            user=myUser,
            password=myPassword,
            database=myDatabase,
        )
    except Error as e:
        print("Error in createConnection()")
        print(e)

def makeQuery(query):
    connection = createConnection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            return "OK"
    except Error as e:
        print(e)
        return "Error"

def selectQuery(query):
    connection = createConnection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except Error as e:
        print(e)
        return "Error"

def createUser(nombre, apellido, edad):
    createUserQuery = f"""
INSERT INTO USUARIO (nombre, apellido, edad) values ('{nombre}', '{apellido}', {edad})
"""
    connection = createConnection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(createUserQuery)
            connection.commit()
            return "OK"
    except Error as e:
        print(e)
        return "Error"
    
def getUsers():
    selectUserQuery = f"""
SELECT * FROM USUARIO
"""
    result = selectQuery(selectUserQuery)
    if result == "Error":
        return result
    else:
        return jsonify(result)
    
def editUserDB(id, nombre, apellido, edad):
    editUserQuery = f"""
UPDATE USUARIO SET nombre = '{nombre}', apellido = '{apellido}', edad = {edad} WHERE id = {id}
"""
    return makeQuery(editUserQuery)

def deleteUserDB(id):
    deleteUserQuery = f"""
DELETE FROM USUARIO WHERE id = {id}
"""
    return makeQuery(deleteUserQuery)