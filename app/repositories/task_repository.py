from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update_task(self, task_id: int, task_data: dict):
        task = self.get_task(task_id)
        for key, value in task_data.items():
            setattr(task, key, value)
        self.db.commit()
        return task

    def delete_task(self, task_id: int):
        task = self.get_task(task_id)
        self.db.delete(task)
        self.db.commit()
        return task

    def list_tasks(self):
        return self.db.query(Task).all()

