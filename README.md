# API-сервис для вопросов и ответов
Тестовое задание

## Назначение

## API-запросы

## Как запустить проект:

Cоздать и активировать виртуальное окружение:
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

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```

