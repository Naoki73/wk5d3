from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin



db = SQLAlchemy()


def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
        
class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.Column(db.String(50), nullable=False)
    Front_Shiny = db.Column(db.String(200), nullable=False)
    Base_ATK = db.Column(db.Integer, nullable=False)
    Base_HP = db.Column(db.Integer, nullable=False)
    Base_DEF = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )

    def __init__(self, name, ability, Front_Shiny, Base_ATK, Base_HP, Base_DEF, user_id):
        self.name = name
        self.ability = ability
        self.Front_Shiny = Front_Shiny
        self.Base_ATK = Base_ATK
        self.Base_HP = Base_HP
        self.Base_DEF = Base_DEF
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
