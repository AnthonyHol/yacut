import random
import string

from .constants import LEN_CUSTOM_ID
from .models import URLMap


def get_short_id(original_url):
    """Функция получения короткой ссылки из случайных символов."""
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    custom_id = "".join(random.choice(chars) for _ in range(LEN_CUSTOM_ID))

    if URLMap.query.filter_by(short=custom_id).first():
        return get_short_id(original_url)

    return custom_id
