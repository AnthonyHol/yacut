from http import HTTPStatus
from re import fullmatch

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_short_id

# todo
# вынести тексты ошибок и прочие постоянные в константы
# рефактор добавления url в бд


@app.route("/api/id/", methods=["POST"])
def create_short_url():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса")

    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    custom_id = data.get("custom_id")
    original_url = data["url"]

    if not custom_id:
        custom_id = get_short_id(original_url)

    if URLMap.query.filter_by(original=original_url).first():
        raise InvalidAPIUsage(message=f'Имя "{custom_id}" уже занято.')

    if not fullmatch(rf"^[A-Za-z0-9]{{1,{16}}}$", custom_id):
        raise InvalidAPIUsage(
            message="Указано недопустимое имя для короткой ссылки"
        )

    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(message=f"Имя {custom_id} уже занято.")

    url = URLMap(original=original_url, short=custom_id)

    db.session.add(url)
    db.session.commit()

    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route("/api/id/<string:short>/", methods=["GET"])
def get_original_url(short):
    url = URLMap.query.filter_by(short=short).first()

    if not url:
        raise InvalidAPIUsage(
            message=f'"{short}" не найден!', status_code=HTTPStatus.NOT_FOUND
        )

    return jsonify({"url": url.original}), HTTPStatus.OK
