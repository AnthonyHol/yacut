from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):
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
                max=16, message=f'Максимальная длина ссылки - 16 символов.'
            ),
            Regexp(
                "^[A-Za-z0-9]*$",
                message="В URL допустимы только буквы A-Z, a-z и цифры 0-9.",
            ),
            Optional(),
        ],
    )
    submit = SubmitField("Создать")
