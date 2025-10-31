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
### Установка зависимостей
Чтобы установить проект, нужно ввести команду  ```make install```, которая запускает ```uv sync``` и устанавливает все зависимости автоматически.
### Запуск игры
Чтобы вызвать точку входа, нужно ввести команду ```make brain-games```, которая запускает ```uv run brain-games```.
### Сборка проекта и установка пакета
Прежде чем публиковать, необходимо осуществить сборку проекта командой  ```make build```, которая выполнит команду ```uv build```.
Установить пакет в операционную систему необходимо с помощью команды ```make package-install ```, которая выполнит  ```uv tool install dist/*.whl```.
### Установка дополнительных зависимостей 
Проверить код на соответствие стандартам нужно с помощью команды ```make lint```, которая выполнит  ```uv run ruff check brain_games```.
### Описание и запуск игр 
#### Игра «Проверка на чётность»
Угадать чётность числа.
После сборки и установки пакета в операционную систему запустите игру командой ```brain-even```.
#### Игра «Калькулятор»
Ввести результат вычисления математического выражения.
После сборки и установки пакета в операционную систему запустите игру командой ```brain-calc```.
#### Игра «НОД»
Найти наибольший делитель двух чисел.
После сборки и установки пакета в операционную систему запустите игру командой ```brain-gcd```.
#### Игра «Арифметическая прогрессия»
Найти пропущенное число в ряде арифметической прогрессии.
После сборки и установки пакета в операционную систему запустите игру командой ```brain-progression```.
#### Игра «Простое ли число?»
Определить, является ли число простым.
После сборки и установки пакета в операционную систему запустите игру командой ```brain-prime```.
## Демонстрация 
[![asciicast](https://asciinema.org/a/tcaInEOHOKPusJlRAPcdaR8qn.svg)](https://asciinema.org/a/tcaInEOHOKPusJlRAPcdaR8qn)
