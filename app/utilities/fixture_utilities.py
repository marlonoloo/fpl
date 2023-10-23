from app.models import Team, Fixture


def get_fixture(team_id, gameweek_id):
    fixture = Fixture.query.filter(
        ((Fixture.home_team_id == team_id) | (Fixture.away_team_id == team_id)) &
        (Fixture.gameweek_id == gameweek_id)
    ).first()

    return fixture


def calculate_team_fixture_difficulty(min_gameweek, max_gameweek):
    teams = Team.query.all()

    team_fixture_difficulties = {}

    for team in teams:
        total_fixture_difficulty = 0

        for gameweek in range(min_gameweek, max_gameweek + 1):
            home_fixtures = Fixture.query.filter_by(gameweek_id=gameweek, home_team_id=team.team_id).all()
            away_fixtures = Fixture.query.filter_by(gameweek_id=gameweek, away_team_id=team.team_id).all()

            for fixture in home_fixtures:
                opponent = fixture.away_team
                fixture_difficulty = opponent.away_difficulty
                total_fixture_difficulty += fixture_difficulty

            for fixture in away_fixtures:
                opponent = fixture.home_team
                fixture_difficulty = opponent.home_difficulty
                total_fixture_difficulty += fixture_difficulty

        team_fixture_difficulties[team.team_name] = total_fixture_difficulty

    sorted_teams = sorted(teams, key=lambda team: team_fixture_difficulties[team.team_name])
    return sorted_teams, team_fixture_difficulties
