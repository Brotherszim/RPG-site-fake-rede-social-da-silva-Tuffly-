from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET","POST"]) #define o url da pagina e os metodos que vai receber
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        return redirect(url_for("login")) #redireciona para login
    return render_template("index.html") #se não receber nada só retorna a página normal

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        return "Você logou, parabéns"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
