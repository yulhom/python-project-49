### Hexlet tests and linter status:
[![Actions Status](https://github.com/yulhom/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/yulhom/python-project-49/actions)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=yulhom_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=yulhom_python-project-49)
## Инструкция по установке
Для работы и установки игр потребуется uv, его можно скачать [отсюда](https://docs.astral.sh/uv/getting-started/installation/).
### Шаг 1. Инициализация проекта
Чтобы инициализировать ваш проект, нужно ввести команду ```uv init```.
### Шаг 2. Установка зависимостей
Чтобы установить проект, нужно ввести команду ```uv sync```.
Если вы используете Makefile, то достаточно ввести команду ```make install```, которая запускает ```uv sync``` и устанавливает все зависимости автоматически.
Команда `install` должна быть определена в Makefile:
```makefile
install:
	uv sync
```
### Шаг 3. Запуск игры
Чтобы вызвать точку входа, нужно ввести команду ```uv run brain-games```.
Если вы используете Makefile, то достаточно ввести команду ```make brain-games```, которая запускает ```uv run brain-games```.
Команда `brain-games` должна быть определена в Makefile:
```makefile
brain-games:
	uv run brain-games
```
### Шаг 4. Сборка проекта
Прежде чем публиковать, необходимо осуществить сборку проекта командой ```uv build```.
Если вы используете Makefile, то достаточно ввести команду ```make build```, которая выполнит команду ```uv build```.
Команда `build` должна быть определена в Makefile:
```makefile
build:
	uv build
```
### Шаг 5. Установка пакета в операционную систему
Установить пакет в операционную систему нужно командой ```uv tool install dist/*.whl```.
Если вы используете Makefile, то достаточно ввести команду ```make package-install ```, которая выполнит  ```uv tool install dist/*.whl```.
Команда `package-install` должна быть определена в Makefile:
```makefile
package-install:
	uv tool install dist/*
```
### Шаг 6. Установка дополнительных зависимостей 
Чтобы подключить библиотеку `prompt` в зависимости, выполните команду ```uv add prompt```.
Для проверки кода по стандартам качества рекомендуется использовать `ruff`.  
Добавьте его в dev-зависимости командой ```uv add --dev ruff```.
Проверить код на соответствие стандартам нужно с помощью команды```uv run ruff check brain_games```.
Если вы используете Makefile, то достаточно ввести команду ```make lint```, которая выполнит  ```uv run ruff check brain_games```.
Команда `lint` должна быть определена в Makefile:
```makefile
lint:
	uv run ruff check brain_games
```
### Шаг 7. Точки входа для игр
В файле `pyproject.toml` необходимо указать точки входа, чтобы игры можно было запускать как команды из терминала.
Точка входа для игры "Проверка на четность" - `brain-even = "brain_games.scripts.brain_even:main"`.
Точка входа для игры "Калькулятор" - `brain-calc = "brain_games.scripts.brain_calc:main"`.
Точка входа для игры "НОД" - `brain-gcd = "brain_games.scripts.brain_gcd:main"`.
Точка входа для игры "Арифметическая прогрессия" - `brain-progression = "brain_games.scripts.brain_progression:main"`.
Точка входа для игры "Простое число" - `brain-prime = "brain_games.scripts.brain_prime:main"`.
После этого вы сможете запустить игры командами  ```uv run brain-even```,  ```uv run brain-calc```, ```uv run brain-gcd```, ```uv run brain-progression```,  ```uv run brain-prime```.
После сборки проекта и установки пакета для запуска игры достаточно ввести команды ```brain-even```, ```brain-calc```, ```brain-gcd```,  ```brain-progression```, ```brain-prime```.
## Демонстрация 
[![asciicast](https://asciinema.org/a/tcaInEOHOKPusJlRAPcdaR8qn.svg)](https://asciinema.org/a/tcaInEOHOKPusJlRAPcdaR8qn)
