# Event Planner

## Описание
Event Planner – это удобное приложение для организации мероприятий, позволяющее создавать, управлять и отслеживать события. Проект разработан с использованием современных технологий и предоставляет интуитивно понятный интерфейс для пользователей.

## Возможности
✅ Создание событий – добавление названия, описания, даты, времени и места.
✅ Управление участниками – приглашение гостей, отслеживание подтверждений.
✅ Категории и теги – сортировка событий по категориям (например, "День рождения", "Конференция").
✅ Напоминания – уведомления о предстоящих событиях.
✅ Гибкие настройки – возможность кастомизировать события под свои нужды.

## Технологии

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django Version](https://img.shields.io/badge/django-3.2-green.svg)
![Django REST](https://img.shields.io/badge/django%20rest%20framework-3.12.4-red.svg)
![Django Channels Rest Framework](https://img.shields.io/badge/django%20channels%20rest-1.2.0-9cf.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg)


### Документация в формате Redoc:
```HTTP
http://127.0.0.1:8000/redoc/
```

### Документация в формате Swagger: 
```HTTP
http://127.0.0.1:8000/swagger/
```

### Чат полозователей доступен: 
```HTTP
http://127.0.0.1:8000/api/v1/chat/
```

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