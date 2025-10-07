from flask import Blueprint, render_template

carregamento_bp = Blueprint("carregamento", __name__)

@carregamento_bp.route("/carregamento", methods=["GET", "POST"])
def carregamento():
    return render_template("carregamento.html")