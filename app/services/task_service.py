from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, db: Session):
        self.repository = TaskRepository(db)

    def create_task(self, title: str, description: str, status: str):
        task = Task(title=title, description=description, status=status)
        return self.repository.create_task(task)

    def get_task(self, task_id: int):
        return self.repository.get_task(task_id)

    def update_task(self, task_id: int, task_data: dict):
        return self.repository.update_task(task_id, task_data)

    def delete_task(self, task_id: int):
        return self.repository.delete_task(task_id)

    def list_tasks(self):
        return self.repository.list_tasks()
