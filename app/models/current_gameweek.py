from app.extensions import db


class CurrentGameweek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameweek_number = db.Column(db.Integer, nullable=False)

    def __init__(self, gameweek_number):
        self.gameweek_number = gameweek_number
