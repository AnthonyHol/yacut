from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import MAX_LEN, MAX_LEN_OUTPUT, REG_EXPRESSION, REG_OUTPUT


class URLForm(FlaskForm):
    """Форма для создания короткой ссылки."""

    original_link = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            URL(message="Введите исходный URL."),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткого URL.",
        validators=[
            Length(
                max=MAX_LEN,
                message=MAX_LEN_OUTPUT,
            ),
            Regexp(
                REG_EXPRESSION,
                message=REG_OUTPUT,
            ),
            Optional(),
        ],
    )
    submit = SubmitField("Создать")
