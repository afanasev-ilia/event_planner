# event_planner

## Описание
Приложение для планирования мероприятий.

Документация в формате Redoc:
```HTTP
http://127.0.0.1:8000/redoc/
```

Документация в формате Swagger: 
```HTTP
http://127.0.0.1:8000/swagger/
```

Чат полозователей доступен: 
```HTTP
http://127.0.0.1:8000/api/v1/chat/
```

## Технологии

Python 3.9.10
Django 3.2
Django REST framework 3.12.4

## Запуск проекта локально

Клонируем репозиторий и переходим в него в командной строке:
```bash
git clone git@github.com:afanasev-ilia/event_planner.git
```
```bash
cd event_planner
```

Запускаем docker-compose:
```bash
docker-compose up -d --build
```

Выполняем миграции:
```bash
docker-compose exec event_planner python manage.py migrate
```

Создаем суперппользователя:
```bash
docker-compose exec event_planner python manage.py createsuperuser
```

Останавливаем собранные контейнеры:
```bash
docker-compose down -v 
```

Для корректной работы чата в тестовом режиме необходимо
добавить JWT-токен в Local storage
```
Token='********************************'
```

## Шаблон наполнения .env
```
SECRET_KEY='********************************'
```

## Автор
Илья Афанасьев