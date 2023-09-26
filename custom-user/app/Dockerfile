FROM python:3.11.5-slim-bookworm

WORKDIR /usr/code/app

RUN apt-get update \
&& apt-get install gcc libpq-dev postgresql netcat-traditional -y \
&& apt-get clean

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./entrypoint.sh /usr/code/app/entrypoint.sh
RUN chmod +x /usr/code/app/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/code/app/entrypoint.sh" ]