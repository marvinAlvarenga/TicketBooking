build:
	docker compose build
test:
	docker compose run --rm api ./scripts/tests.sh
lint:
	docker compose run --rm api ./scripts/lint.sh