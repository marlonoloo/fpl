from flask import render_template, request
from app.main import bp
from app.utilities.fixture_utilities import (calculate_team_fixture_difficulty,
                                             get_fixture)
from app.models import CurrentGameweek


@bp.route('/', methods=['GET'])
def fixtures():
    current_gameweek = CurrentGameweek.query.first()
    current_gameweek = current_gameweek.gameweek_number

    min_gameweek = int(request.args.get('min_gameweek', current_gameweek))
    max_gameweek = int(request.args.get('max_gameweek', min_gameweek + 5))

    sorted_teams, team_fixture_difficulties = calculate_team_fixture_difficulty(min_gameweek, max_gameweek)

    return render_template('index.html', teams=sorted_teams, fixtures=fixtures,
                           team_difficulties=team_fixture_difficulties,
                           min_gameweek=min_gameweek,
                           max_gameweek=max_gameweek, get_fixture=get_fixture)
