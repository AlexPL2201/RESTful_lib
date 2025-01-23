# Book API

Это простой API для управления книгами, разработанный с использованием Django и Django REST Framework. API позволяет добавлять, получать, обновлять и удалять книги.

## Как запустить проект

### Предварительные требования

- Python 3.8 или выше
- pip
- Git

### Клонирование репозитория

Сначала клонируйте репозиторий:
```
git clone https://github.com/username/book-api.git
cd RESTful_lib/rest_lib
```

### Установка зависимостей

Создайте виртуальное окружение и активируйте его:
```
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```

Установите необходимые библиотеки:
```
pip install -r requirements.txt
```

### Настройка базы данных

1. Примените миграции:
```
python manage.py migrate
```

### Запуск сервера

Запустите сервер разработки:
```
python manage.py runserver
```

## Описание API и его эндпоинтов

### Эндпоинты

#### 1. Получить список всех книг

- **URL:** /books/
- **Метод:** GET
- **Ответ:**

#### 2. Добавить новую книгу

- **URL:** /books/
- **Метод:** POST
- **Тело запроса:**

#### 3. Получить информацию о книге по ID

- **URL:** /books/{id}/
- **Метод:** GET
- **Ответ:**

#### 4. Обновить информацию о книге

- **URL:** /books/{id}/
- **Метод:** PUT
- **Тело запроса:**

#### 5. Удалить книгу

- **URL:** /books/{id}/
- **Метод:** DELETE
- **Ответ:** 204 No Content


## Используемые технологии и библиотеки

- [Django](https://www.djangoproject.com/) - веб-фреймворк для разработки.
- [Django REST Framework](https://www.django-rest-framework.org/) - библиотека для создания RESTful API.
- [Python](https://www.python.org/) - язык программирования.
- [SQLite](https://www.sqlite.org/index.html) - легковесная база данных (по умолчанию).
