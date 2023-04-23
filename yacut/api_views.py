from http import HTTPStatus
from re import fullmatch

from flask import jsonify, request

from . import app
from .constants import (
    ID_NOT_FOUND,
    INVALID_NAME,
    NO_DATA,
    NO_REQUIRED_FIELD,
    REG_EXPRESSION,
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_short_id


@app.route("/api/id/", methods=["POST"])
def create_short_url():
    """Функция создания короткого URL."""
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage(NO_DATA)

    if "url" not in data:
        raise InvalidAPIUsage(NO_REQUIRED_FIELD)

    custom_url = data.get("custom_id")
    original_url = data["url"]

    if not custom_url:
        custom_url = get_short_id(original_url)

    if URLMap.query.filter_by(original=original_url).first():
        raise InvalidAPIUsage(message=f'Имя "{custom_url}" уже занято.')

    if not fullmatch(REG_EXPRESSION, custom_url):
        raise InvalidAPIUsage(message=INVALID_NAME)

    if URLMap.query.filter_by(short=custom_url).first():
        raise InvalidAPIUsage(message=f"Имя {custom_url} уже занято.")

    url = URLMap(original=original_url, short=custom_url)
    URLMap.add_object(url)

    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route("/api/id/<string:short>/", methods=["GET"])
def get_original_url(short):
    """Функция получения оригинального URL по короткой версии."""

    url = URLMap.query.filter_by(short=short).first()

    if not url:
        raise InvalidAPIUsage(
            message=ID_NOT_FOUND, status_code=HTTPStatus.NOT_FOUND
        )

    return jsonify({"url": url.original}), HTTPStatus.OK
