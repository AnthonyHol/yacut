# Проект YaCut
## Спринт 21 — yacut

## Описание проекта
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Технологии
- Python 3.9.13
- Flask 2.0.1
- Flask-Migrate 3.1.0
- Flask-SQLAlchemy 2.5.1
- Flask-WTF 1.0.0
- Jinja2 3.1.2
- click 8.1.3

## Запуск проекта

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone 

```
cd yacut

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

3. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Создать и заполнить .env по шаблону ниже:

```
FLASK_APP=yacut
FLASK_ENV=<production или development>
DATABASE_URI=<sqlite:///db.sqlite3 или адрес другой БД>
SECRET_KEY=<секретный ключ>
```
5. Подключить БД (для sqlite3):

* запустить оболочку: ```flask shell```;
* выполнить команды:

```
>>>form yacut import db
>>>db.create_all()
```
* в корне проекта появится файл ```db.sqlite3```.

6. Запустить приложение: ```flask run```.

#### Эндпоинты API


```api/id/``` — POST-запрос на создание новой короткой ссылки.

```/api/id/<short_id>/``` — GET-запрос на получение оригинальной ссылки по короткой версии.

Более подробную информацию можно посмотреть в спецификации API ```openapi.yml```. Для удобного просмотра можно использовать ```https://editor.swagger.io/```.
