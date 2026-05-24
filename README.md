# Решение заданий по теме "Декораторы"

## Описание
Решение задания 1 в decorator_1ex.py

Решение задания 2 в decorators.py

Решение задания 3 в main.py. По условиям задания необходимо 
применить написанный логгер к приложению из любого предыдущего д/з. 
Был выбран проект из домашнего задания по теме "Import.Module.Package".
Каждая функция, вызываемая из main.py задекорирована логгером из decorators.py.
Файлы с логами сохраняются в \logs

## Стуктура проекта
```
project/
├── application/ # Пакет с бизнес-логикой
│ ├── init.py # Маркер пакета
│ ├── salary.py # Функция calculate_salary
│ └── db/ # Подпакет для БД
│ ├── init.py # Маркер подпакета
│ └── people.py # Функция get_employees
│
├── decorators.py # Решение задания 2 (Декоратор logger)
│
├── logs/ # Папка для логов
│ ├── salary.log # Лог calculate_salary
│ └── people.log # Лог get_employees
│
├── main.py # Решение задания 3 (Главный файл проекта д/3)
│
├── decorator_1ex.py # Решение задания 1
├── log_1.log # Лог hello_world
├── log_2.log # Лог summator
├── log_3.log # Лог div
└── main.log # Лог Задания 1
...