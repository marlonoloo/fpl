from app.extensions import db


class Gameweek(db.Model):
    gameweek_id = db.Column(db.Integer, primary_key=True)
    gameweek_number = db.Column(db.Integer, nullable=False)
