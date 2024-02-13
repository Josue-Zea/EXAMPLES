from flask import Flask, request, Response
from connection import createUser, getUsers, editUserDB, deleteUserDB

app=Flask(__name__)

@app.route("/user", methods = ['GET', "POST", "PUT", "DELETE"])
def index():
    if request.method == 'GET':
        return getUsers()
    if request.method == 'POST':
        content = request.json
        return createUser(content["nombre"], content["apellido"], content["edad"])
    if request.method == 'PUT':
        content = request.json
        return editUserDB(content["id"], content["nombre"], content["apellido"], content["edad"])
    if request.method == 'DELETE':
        content = request.json
        return deleteUserDB(content["id"])
    
@app.route("/prueba", methods = ["POST"])
def prueba():
    content = request.json
    if(content["nombre"] == "Josue"):
        return Response("{'parametro1':'valorparam1'}", status=200, mimetype='application/json')
    if(content["nombre"] == "Jeanete"):
        return Response(f"El nombre es {content["nombre"]}", status=400, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=3000)