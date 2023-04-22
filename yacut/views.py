from http import HTTPStatus

from flask import flash, redirect, render_template, url_for

from yacut.forms import URLForm
from yacut.models import URLMap

from . import app, db
from .utils import get_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = URLForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if URLMap.query.filter_by(original=form.original_link.data).first():
            flash("Такая ссылка уже имеет укороченную версию!")

            return render_template("content.html", form=form)

        if URLMap.query.filter_by(short=custom_id).first():
            flash(f"Имя {custom_id} уже занято!")

            return render_template("content.html", form=form)

        if not custom_id:
            custom_id = get_short_id(form.original_link)

        url = URLMap(original=form.original_link.data, short=custom_id)

        db.session.add(url)
        db.session.commit()

        return (
            render_template("content.html", form=form, short=custom_id),
            HTTPStatus.OK,
        )

    return render_template("content.html", form=form), HTTPStatus.OK


@app.route("/<string:short>", methods=["GET"])
def redirect_view(short):
    return (
        redirect(URLMap.query.filter_by(short=short).first_or_404().original),
        HTTPStatus.FOUND,
    )
