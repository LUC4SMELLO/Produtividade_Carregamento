from flask import Flask

from routes.homepage import homepage_bp
from routes.cadastro import cadastro_bp
from routes.login import login_bp

app = Flask(__name__)
app.secret_key = "secret_key"

app.register_blueprint(homepage_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)