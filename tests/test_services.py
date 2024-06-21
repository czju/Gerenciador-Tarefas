import pytest
from app.services.task_service import TaskService
from app.schemas import TaskCreate, TaskUpdate


@pytest.fixture(scope="module")
def test_task_service(test_db):
    return TaskService(db=test_db)


def test_create_task_service(test_task_service):
    task_data = TaskCreate(title="Service Task", description="Service Description", status="Pendente")
    task = test_task_service.create_task(task_data)
    assert task.title == "Service Task"
    assert task.description == "Service Description"
    assert task.status == "Pendente"


def test_get_tasks_service(test_task_service):
    tasks = test_task_service.get_tasks()
    assert len(tasks) >= 1


def test_update_task_service(test_task_service):
    task_data = TaskCreate(title="Task to Update", description="Update this task", status="Pendente")
    task = test_task_service.create_task(task_data)

    update_data = TaskUpdate(title="Updated Service Task", description="Updated Service Description",
                             status="Concluída")
    updated_task = test_task_service.update_task(task.id, update_data)
    assert updated_task.title == "Updated Service Task"
    assert updated_task.description == "Updated Service Description"
    assert updated_task.status == "Concluída"


def test_delete_task_service(test_task_service):
    task_data = TaskCreate(title="Task to Delete", description="Delete this task", status="Pendente")
    task = test_task_service.create_task(task_data)

    test_task_service.delete_task(task.id)
    task = test_task_service.get_task_by_id(task.id)
    assert task is None
