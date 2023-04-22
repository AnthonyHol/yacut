import random
import string

from .models import URLMap


def get_short_id(original_link):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    short_id = "".join(random.choice(chars) for _ in range(6))

    if URLMap.query.filter_by(short=short_id).first():
        return get_short_id(original_link)

    return short_id
