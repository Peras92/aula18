from flask import Flask, render_template, request, redirect, url_for
from sqla_wrapper import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy("sqlite:///db.sqlite")

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utilizador = db.Column(db.String, unique=False)
    texto = db.Column(db.String, unique=False)

db.create_all()



@app.route("/")
def index():
    mensagem = db.query(Mensagem).all()
    return render_template("index.html", mensagem=mensagem)

@app.route("/add-message", methods=["POST"])
def add_message():
    utilizador = request.form.get("utilizador")
    texto = request.form.get("texto")

    mensagem = Mensagem(utilizador=utilizador, texto=texto)
    mensagem.save()

    return redirect("/")


if __name__ == '__main__':
    app.run()