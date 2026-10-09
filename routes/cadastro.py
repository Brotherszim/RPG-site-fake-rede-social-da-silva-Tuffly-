
from flask import Blueprint, render_template, request, redirect, url_for
from services.cadastro_service import verificar_cadastro

cadastro_bp = Blueprint("cadastro", __name__) #Cria o blueprint que vai ser chamado no app.py

@cadastro_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confSenha")

        verificarCadastro = verificar_cadastro(nome,email,senha,confirmar_senha)

        if "válido" in verificarCadastro:
            return redirect(url_for("login.login"))
        else:
            return verificarCadastro, 400

        

    return render_template("index.html")
