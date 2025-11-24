from flasgger import Swagger
from flask import Flask

import config

app = Flask(__name__)

app.config.from_object(config)

@app.route("/")
def home():
    return "Página Inicial"


if __name__ == "__main__":
    app.run(debug=True)
