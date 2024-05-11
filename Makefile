cheers:
	@echo "Na zdraví! 🍺"

dev:
	@docker compose -f docker-compose.yml up --build

run:
	@docker compose -f docker-compose.yml up --build -d

stop:
	@docker compose -f docker-compose.yml down

down:
	@docker compose -f ./docker-compose.yml down --remove-orphans

cleaner:
	@vulture . --exclude .venv
