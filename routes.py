from flask import Flask, request

app =  Flask("python-api-with-flask")

usuarios = []

@app.route("/olamundo", methods=["GET"])
def olaMundo():
  return { "OK": 200 }


@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario(usuario={ "name": "Douglas", "lastName": "Lopes"}):
  usuario = request.get_json()
  usuarios.append(usuario)

  return { "usuario": usuario }


@app.route("/listar/usuarios", methods=["GET"])
def listarUsuarios():
  return { "usuarios": usuarios }


app.run()
