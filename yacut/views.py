from http import HTTPStatus

from flask import flash, redirect, render_template

from yacut.forms import URLForm
from yacut.models import URLMap

from . import app, db
from .utils import get_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    """Вью-функция для создания короткого URL."""
    form = URLForm()

    if form.validate_on_submit():
        custom_url = form.custom_id.data
        original_url = form.original_link.data

        if URLMap.query.filter_by(original=original_url).first():
            flash(f"Имя {custom_url} уже занято!")

            return render_template("content.html", form=form)

        if URLMap.query.filter_by(short=custom_url).first():
            flash(f"Имя {custom_url} уже занято!")

            return render_template("content.html", form=form)

        if not custom_url:
            custom_url = get_short_id(original_url)

        url = URLMap(original=original_url, short=custom_url)

        db.session.add(url)
        db.session.commit()

        return (
            render_template("content.html", form=form, short=custom_url),
            HTTPStatus.OK,
        )

    return render_template("content.html", form=form), HTTPStatus.OK


@app.route("/<string:short>", methods=["GET"])
def redirect_view(short):
    """Вью-функция для получения оригинального URL по короткой версии."""
    return (
        redirect(URLMap.query.filter_by(short=short).first_or_404().original),
        HTTPStatus.FOUND,
    )
