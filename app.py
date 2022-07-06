import re
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Heroes
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/HeroesBack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route("/Heroes", methods=["POST", "GET"])
def heroes():
    if request.method == "GET":
        heroes = Heroes.query.all()
        results = list(map(lambda heroes: heroes.serialize(), heroes))
        return jsonify(results)
    
    if request.method == "POST":
        id_name = request.json.get("id_name")
        type = request.json.get("type")
        superhero = request.json.get("superhero")
        alterego= request.json.get("alter_ego")
        first_appearance= request.json.get("first_appearance")
        character= request.json.get("character")
        publisher = request.json.get("publisher")
    
    heroes_exist = Heroes.query.filter_by(superhero=superhero).first()
    
    if heroes_exist != None:
            return jsonify("Éste Heroe ya fue agregado."), 404
    else:
        event = Heroes()
        event.id_name = id_name
        event.type = type
        event.superhero = superhero
        event.alter_ego = alterego
        event.first_appearance = first_appearance
        event.character = character
        event.publisher = publisher
        db.session.add(event)
        db.session.commit()
        return jsonify({
            "msg": "Heroe Creado con Exito"
        }), 200


if __name__ == "__main__":
    app.run(host ="localhost", port = 8010)
