FROM python:3.10.10-bullseye as develop

RUN apt update

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .
RUN poetry install

RUN chmod -R +x ./scripts
CMD ["./scripts/entrypoint.sh"]
