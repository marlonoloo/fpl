from app.extensions import db


class Fixture(db.Model):
    fixture_id = db.Column(db.Integer, primary_key=True)
    gameweek_id = db.Column(db.Integer, db.ForeignKey('gameweek.gameweek_id'),
                            nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'),
                             nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'),
                             nullable=False)

    # Define relationships with the Team and Gameweek tables
    home_team = db.relationship('Team', foreign_keys=[home_team_id])
    away_team = db.relationship('Team', foreign_keys=[away_team_id])
    gameweek = db.relationship('Gameweek')
