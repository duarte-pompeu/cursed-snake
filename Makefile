# inspired by https://gist.github.com/trickeydan/0bace38b00ba8488b5aa1f178b1f3f33

.PHONY: all install run clean lint type test test-cov help help2
.DEFAULT_GOAL:=help

CMD:=poetry
PYMODULE:=src/
TESTS:=tests

all: install run ## Installs and runs locally

install: ## installs necessary packages
	$(CMD) update
	$(CMD) install

run: ## runs the program locally
	$(CMD) run python src/main.py

run-win: ## runs the program locally, with Windows compatibility a layer (WINPTY)
	winpty $(CMD) run python src/main.py

clean: ## Does nothing at the moment

# lint:
# 	$(CMD) flake8 $(PYMODULE) $(TESTS) $(EXTRACODE)

# type:
# 	$(CMD) mypy $(PYMODULE) $(TESTS) $(EXTRACODE)

# test:
# 	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

# test-cov:
# 	$(CMD) pytest --cov=$(PYMODULE) $(TESTS) --cov-report html

# isort:
# 	$(CMD) isort --recursive $(PYMODULE) $(TESTS) $(EXTRACODE)


build: ## builds a docker image for cursed-snake
	docker build . -t "cursed-snake:latest"

up: ## runs a container with the docker image
	docker container run --name cursed-snake -i -t cursed-snake:latest --rm 

up-win: ## runs a container with the docker images, with a Windows compatibility layer (WINPTY)
	winpty docker container run --name cursed-snake -i -t cursed-snake:latest --rm

# inspired by https://gist.github.com/prwhite/8168133#gistcomment-2833138
help: ## Displays help message (this)
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)