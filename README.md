# TO-DO LIST

REST API для управления задачами (To-Do list) с возможностью:
- Создания, чтения, обновления и удаления задач
- Фильтрации задач по статусу и приоритету
---
## Автор
**Диана Шакирова**  
[![GitHub](https://img.shields.io/badge/GitHub-DianaShakirovaM-black)](https://github.com/DianaShakirovaM)  
---
## Установка

### Технологии
- Backend: Django 3.2 + Django REST Framework
- Аутентификация: Djoser
- Python 3.9+
---
### Локальный запуск
1. Клонируйте репозиторий:
```bash
   git clone https://github.com/DianaShakirovaM/task_3.git
   cd task_4
```
2. Установите зависимости:
```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```
3. Примените миграции:
```bash
  python manage.py migrate
```
4. Запустите сервер:
```bash
  python manage.py runserver
```
---
## Примеры запросов
### Посмотреть все задачи:
```http
Content-Type: application/json
Authorization: Token ваш_токен
GET /api/tasks/
```
### Создать задачу
```http
Content-Type: application/json
Authorization: Token ваш_токен
POST /api/tasks/
```
