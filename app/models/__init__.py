from flask import Blueprint

bp = Blueprint('models', __name__)

from app.models.teams import Team
from app.models.fixtures import Fixture
from app.models.gameweeks import Gameweek
from app.models.results import Result
from app.models.current_gameweek import CurrentGameweek
