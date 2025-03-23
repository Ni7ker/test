from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()
tasks = []
current_id = 1  # Для генерации уникальных ID

class Task(BaseModel):
    title: str
    description: str
    deadline: str

# Валидация формата дедлайна
def validate_deadline(deadline: str) -> bool:
    try:
        datetime.strptime(deadline, "%d-%m-%Y")
        return True
    except ValueError:
        return False

@app.post("/tasks")
def add_task(task: Task):
    global current_id
    if not validate_deadline(task.deadline):
        raise HTTPException(status_code=400, detail="Неверный формат дедлайна. Используйте DD-MM-YYYY.")
    tasks.append({
        "id": current_id,
        "title": task.title,
        "description": task.description,
        "deadline": task.deadline
    })
    current_id += 1
    return {"message": "Задача добавлена"}

@app.get("/tasks")
def get_tasks():
    # Сортировка по дедлайну (ближайшие сверху)
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], "%d-%m-%Y"))
    return sorted_tasks

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    initial_length = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == initial_length:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return {"message": "Задача удалена"}

# Комментарии:
# 1. Список tasks хранит задачи в памяти.
# 2. current_id гарантирует уникальность ID.
# 3. Сортировка по дедлайну через преобразование строки в datetime.

# Улучшения для продакшена:
# 1. Добавить базу данных (PostgreSQL/Redis).
# 2. Реализовать аутентификацию (JWT/OAuth2).
# 3. Настроить логирование и мониторинг (Prometheus/Grafana).
# 4. Добавить тесты (pytest).
# 5. Использовать Celery для асинхронных задач.