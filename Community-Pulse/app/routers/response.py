from flask import Blueprint

responses_bp = Blueprint('response', __name__)


@responses_bp.route('/', methods=['GET'])
def get_response():
    return "Статистика всех ответов"


@responses_bp.route('/', methods=['POST'])
def add_response():
    return "Ответ добавлен"