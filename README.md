## Использование

Установка библиотек

`pip install pipenv`
`pipenv install`

Docker build
`docker build -t poll_api .`

Docker run
`docker run -p 8888:8888 poll_api`

Чтобы получить токен авторизации, надо создать суперюзера и получить токен с помощью api/user/token.
Чтобы использовать токен в сваггере, надо нажать на Authorize и вставить **Bearer token**

## Документация


Техническая документация описана в сваггере

Доступ к сваггеру http://localhost:8888/swagger
