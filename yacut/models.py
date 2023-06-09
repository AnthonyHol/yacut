from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """Модель для работы с оригинальными и короткими URL."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), index=True, nullable=False)
    short = db.Column(db.String(16), index=True, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Метод преобразования объекта URLMap в словарь."""

        return dict(
            url=self.original,
            short_link=url_for(
                "redirect_view", short=self.short, _external=True
            ),
        )

    def add_object(self):
        """Метод создания объекта URLMap."""

        url = URLMap(original=self.original, short=self.short)

        db.session.add(url)
        db.session.commit()
