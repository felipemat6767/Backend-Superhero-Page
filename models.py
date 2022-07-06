from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Heroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_name = db.Column(db.String(30), nullable=False)
    superhero = db.Column(db.String(50), nullable=False)
    alter_ego = db.Column(db.String(30), nullable=False)
    first_appearance = db.Column(db.String(100), nullable=False)
    character = db.Column(db.String(400), nullable=False)
    publisher = db.Column(db.String(90), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return "<Heroes %r>" % self.name
    
    def serialize(self):
        return {
            'id': self.id,
            'type':self.type,
            'character':self.character,
            'alter_ego':self.alter_ego,
            'superhero':self.superhero,
            'id_name':self.id_name,
            "publisher": self.publisher,
            'first_appearance':self.first_appearance
        }
    def serialize_just_name(self):
        return {
            'id':self.id,
             'superhero':self.superhero
        }