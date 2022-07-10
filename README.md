# yamdb_final
yamdb_final
![example workflow](https://github.com/vincentvega614/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Адрес с работающим приложением
http://130.193.42.175/
http://130.193.42.175/redoc/
http://130.193.42.175/admin/
http://130.193.42.175/api/v1/

### Описание проекта:

Данный проект является амбициозным и развивающимяся аналогом всем известных соц.сетей, где любой пользователь может зарегистрироваться и вести свой блог, комментировать посты других пользователей, а также подписываться на них и следить за обновлениями. В проекте также релизован API, благодаря которому можно выполнять все теже действия.
Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/vincentvega614/yamdb_final.git

cd yamdb_final

Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:

pip install -r api_yatube/requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python3 manage.py runserver

### Примеры запросов к API:

http://127.0.0.1:8000/api/v1/posts/

GET-запрос для получения всех постов

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

http://127.0.0.1:8000/api/v1/posts/

POST-запрос для создания поста от пользователя под которым был отправлен запрос

Более детально с работой API можно ознакомится по в документации.

http://127.0.0.1:8000/redoc/

Создание образа

создайте образ

docker-compose up -d --build

выполните миграции

docker-compose exec web python manage.py migrate

создайте суперпользователя

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input

### Информаци я об авторе

Данный проект является учебным. Все пожелания и информацию об обнаруженных ошибках можно отправлять: e-mail: vincentvega-94@yandex.ru