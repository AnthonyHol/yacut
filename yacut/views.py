from flask import flash, redirect, render_template, url_for

from yacut.forms import URLForm
from yacut.models import URLMap

from . import app, db
from .utils import get_short_id


@app.route('/', methods=["GET", "POST"])
def index_view():
    form = URLForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if URLMap.query.filter_by(original=form.original_link.data).first():
            flash('Такая ссылка уже имеет укороченную версию!')

            return render_template('content.html', form=form)

        if not custom_id:
            custom_id = get_short_id(form.original_link)

        url = URLMap(original=form.original_link.data, short=custom_id)

        db.session.add(url)
        db.session.commit()

        return redirect(url_for('index_view', form=form))

    return render_template('content.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    original_url = URLMap.query.filter_by(short=short).first_or_404().original

    return redirect(original_url)
