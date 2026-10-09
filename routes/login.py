
from flask import Blueprint, render_template, request

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # Futuramente, verificar as credenciais
        # usando os dados salvos no banco.

        return "Você logou, parabéns!"

    return render_template("login.html")
