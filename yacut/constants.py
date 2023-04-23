# validation vars
REG_EXPRESSION = rf"^[A-Za-z0-9]{{1,{16}}}$"
LEN_CUSTOM_ID = 6
MAX_LEN = 16

# exceptions output
NO_DATA = "Отсутствует тело запроса"
NO_REQUIRED_FIELD = '"url" является обязательным полем!'
INVALID_NAME = "Указано недопустимое имя для короткой ссылки"
ID_NOT_FOUND = "Указанный id не найден"
MAX_LEN_OUTPUT = f"Максимальная длина ссылки - {MAX_LEN} символов."
REG_OUTPUT = "В URL допустимы только буквы A-Z, a-z и цифры 0-9."
