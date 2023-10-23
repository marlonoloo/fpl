from app.extensions import db


class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    team_image = db.Column(db.String(100))
    home_difficulty = db.Column(db.Integer)
    away_difficulty = db.Column(db.Integer)
    abbreviation = db.Column(db.String(10), nullable=True)
