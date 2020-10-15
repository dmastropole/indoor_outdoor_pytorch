# DOCKER TASKS
build:
	docker-compose build

up:
	docker-compose up

run:
	docker-compose run --rm main

download-data:
	docker-compose run --rm main bash bin/download.sh

transform-data:
	docker-compose run --rm main python bin/make_datasets.py

data: download-data transform-data

test:
	docker-compose run --rm main pytest

action: build test

down:
	docker-compose down

prune:
	docker system prune -f

kill-tmux:
	tmux kill-server

clean: down kill-tmux prune
