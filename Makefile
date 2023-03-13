build:
	docker compose build
test:
	docker compose run --rm api ./scripts/tests.sh
lint:
	docker compose run --rm api ./scripts/lint.sh
format:
	docker compose run --rm api ./scripts/format.sh
migrations:
	docker compose run --rm api alembic revision --autogenerate
migrate:
	docker compose run --rm api alembic upgrade head
resetdb:
	docker compose run --rm api alembic downgrade base