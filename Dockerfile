FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /api

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /api/
RUN pipenv install --system

# Copy project
COPY . /api/

EXPOSE 8888

CMD ["python", "polls_project/manage.py", "runserver", "0.0.0.0:8888"]