from app.extensions import db


class Result(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    fixture_id = db.Column(db.Integer, db.ForeignKey('fixture.fixture_id'),
                           nullable=False)
    home_team_score = db.Column(db.Integer, nullable=False)
    away_team_score = db.Column(db.Integer, nullable=False)

    # Define a relationship with the Fixture table
    fixture = db.relationship('Fixture')
