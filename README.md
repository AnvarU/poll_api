## Usage

To install libraries

`pip install pipenv`
`pipenv install`

Docker build
`docker build -t poll_api .`

Docker run
`docker run -p 8888:8888 poll_api`

To obtain auth token, you need to create django superuser with `python manage.py createsuperuser` and get auth with route `api/user/token`
To use this token in swagger, you need to press Authorize and paste **Bearer <token>**

## Documentation


You can see documentation in swagger

Access to swagger http://localhost:8888/swagger
