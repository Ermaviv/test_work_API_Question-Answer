# API-сервис для вопросов и ответов
Тестовое задание

## Назначение
Сервис представляет собой систему вопросов и ответов на них

## API-запросы

- Вопросы (Questions):
- - GET `/questions/` — список всех вопросов
- - POST `/questions/` — создать новый вопрос
- - GET `/questions/{id}` — получить вопрос и все ответы на него
- - DELETE `/questions/{id}` — удалить вопрос (вместе с ответами)


- Ответы (Answers):
- - POST `/questions/{id}/answers/` — добавить ответ к вопросу
- - GET `/answers/{id}` — получить конкретный ответ
- - DELETE `/answers/{id}` — удалить ответ

## Примеры API-запросов

- Список вопросов и ответов на них
```shell
http://127.0.0.1:8000/api/questions/
```

- Выбор вопроса с идентификатором "1" с ответов на него
```shell
http://127.0.0.1:8000/api/questions/1
```

- Добавить ответ через POST запрос к 1-ому вопросу
```shell
http://127.0.0.1:8000/api/questions/1/answers/ 
```


## Как запустить проект:

Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
```
* Для пользователей Linux/macOS

```bash
source venv/bin/activate
```

* Для пользователей Windows
```bash
source venv/scripts/activate
```
Обновить пакетный менеджер pip
```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```
Создать миграции

```bash
python main_app/manage.py makemigrations
```

Выполнить миграции:

```bash
python main_app/manage.py migrate
```

Запустить проект:

```bash
python main_app/manage.py runserver
```

