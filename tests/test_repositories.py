import pytest
from app.repositories.task_repository import TaskRepository
from app.models.task_model import Task
from sqlalchemy.orm import Session


@pytest.fixture
def repo(test_db: Session):
    return TaskRepository(test_db)


def test_create_task(repo: TaskRepository):
    task_data = {"title": "Test Task", "description": "Test Description", "status": "Pendente"}
    task = repo.create_task(task_data)

    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == "Pendente"


def test_get_task(repo: TaskRepository):
    task_data = {"title": "Task to Get", "description": "Get this task", "status": "Pendente"}
    task = repo.create_task(task_data)

    retrieved_task = repo.get_task(task.id)
    assert retrieved_task
    assert retrieved_task.title == "Task to Get"


def test_update_task(repo: TaskRepository):
    task_data = {"title": "Task to Update", "description": "Update this task", "status": "Pendente"}
    task = repo.create_task(task_data)

    updated_data = {"title": "Updated Task", "description": "Updated Description", "status": "Concluída"}
    updated_task = repo.update_task(task.id, updated_data)

    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated Description"
    assert updated_task.status == "Concluída"


def test_delete_task(repo: TaskRepository):
    task_data = {"title": "Task to Delete", "description": "Delete this task", "status": "Pendente"}
    task = repo.create_task(task_data)

    repo.delete_task(task.id)
    deleted_task = repo.get_task(task.id)
    assert deleted_task is None
