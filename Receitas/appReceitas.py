from flasgger import Swagger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False)
    
@app.route("/")
def home():
    return "Página Inicial"


if __name__ == "__main__":
    #app.run(debug=True)
    with app.app_context():
        db.create_all()
        print('Branco de dados criado!')
    