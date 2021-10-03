# Тестовое задание для компании Bcraft на позицию Junior Backend-разработчик

## Задача
Нужно разработать микросервис для счетчиков статистики. Сервис должен уметь взаимодействовать с клиентом при помощи REST API


## Как запустить проект:
    
1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/Drag0nfather/bcraft_test_task
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
4) Добавьте в директорию bcraft_test_task/bcraft файл .env с необходимыми данными для использования БД PostgresSql, а именно:
```
NAME=
DB_USER=
PASSWORD=
HOST=127.0.0.1
PORT=5432
```
5) По желанию можно загрузить тестовые данные для тестирования приложения. Для этого нужно:
```
python3 manage.py shell
    from django.contrib.contenttypes.models import ContentType
    ContentType.objects.all().delete()
    quit()
python manage.py loaddata dump.json 
```
6) Запустить сервер командой:
```
python3 manage.py runserver
```
7) Сервер будет доступен по адресу 127.0.0.1. Для доступа в админ-панель используйте:
```
login: admin
password: admin
```
8) Если не было произведено загрузки тестовых данных, нужно:
```
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
9) Для тестирования приложения нужно:
```
python3 manage.py test
```

## Методы Api:
Для отправки запроса следует использовать:
```
127.0.0.1/statistic/
```
1) Post-запрос на statistic/ используется для сохранения статистики. Принимает в body обязательный аргумент date и необязательные аргументы views, clicks и cost

    Пример запроса(cUrl):
   ```
   curl --location --request POST '127.0.0.1:8000/statistic/' \
   --form 'date="2021-10-02"' \
   --form 'views="69123123"' \
   --form 'cost="1212312123"' \
   --form 'clicks="123156"'
   ```

2) Get-запрос на statistic/ используется для показа статистики. Статистика агрегируется по дате. Может принимать query-параметры 'from' и 'to' - дата начала и окончания выборки статистики. Если не указывать параметры - вернется вся статистика.

    Пример запроса(cUrl):
    ```
   curl --location --request GET '127.0.0.1:8000/statistic/?from=2021-10-01&to=2021-10-08'
    ```

3) Delete-запрос на statistic/ используется для удаления всей статистики.

    Пример запроса(cUrl):
   ```
   curl --location --request DELETE '127.0.0.1:8000/statistic/'
   ```