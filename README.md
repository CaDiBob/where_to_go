# Куда пойти — Москва глазами Артёма
Сайт о самых интересных местах в Москве. Авторский проект Артёма.

[демо сайта на pythonanywhere.com](https://cadibob.pythonanywhere.com/)

## Как установить

Python 3 должен быть установлен, затем используйте `pip`:

```bash
pip install -r requirements.txt
```

Все чувствительные данные прячем в `.env` файл.

```
DEBUG=True
CSRF_COOKIE_SECURE=позволит обеспечить пересылку данных cookies только через протокол HTTPS противоположно DEBUG
SESSION_COOKIE_SECURE=позволит обеспечить пересылку данных cookies только через протокол HTTPS противоположно DEBUG
SECURE_SSL_REDIRECT=используется для перенаправления всех запросов с HTTP на HTTPS противоположно DEBUG.
SECRET_KEY=секретный ключ
ALLOWED_HOSTS=Ваши адреса сайтов
```

## Как запустить

Запуск тестового сервера:

```bash
python manage.py runserver
```
Создать суперпользователя для панели администратора:

```bash
python manage.py createsuperuser
```

Для загрузки json файлов из интернета:

```bash
python manage.py load_place http://адрес/файла.json
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
