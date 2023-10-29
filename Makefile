BSON_PATH = <путь к вашему .bson файлу>

# Default rule
all: up

# Docker commands
up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

# Import initial data to MongoDB
import-data:
	docker exec -it mongodb mongorestore --db mydatabase --collection sample_collection $(BSON_PATH)

# Utility commands
logs:
	docker-compose logs -f

