import pytest
from httpx import AsyncClient

from app.main import app
from app.schemas import TaskCreate, TaskUpdate


@pytest.mark.asyncio
async def test_create_task(test_app: AsyncClient):
    response = await test_app.post("/tasks/",
                                   json={"title": "Test Task", "description": "Test Description", "status": "Pendente"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "Test Description"
    assert response.json()["status"] == "Pendente"


@pytest.mark.asyncio
async def test_read_tasks(test_app: AsyncClient):
    response = await test_app.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_update_task(test_app: AsyncClient):
    create_response = await test_app.post("/tasks/", json={"title": "Task to Update", "description": "Update this task",
                                                           "status": "Pendente"})
    task_id = create_response.json()["id"]

    update_data = {"title": "Updated Task", "description": "Updated Description", "status": "Concluída"}
    response = await test_app.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["description"] == "Updated Description"
    assert response.json()["status"] == "Concluída"


@pytest.mark.asyncio
async def test_delete_task(test_app: AsyncClient):
    create_response = await test_app.post("/tasks/", json={"title": "Task to Delete", "description": "Delete this task",
                                                           "status": "Pendente"})
    task_id = create_response.json()["id"]

    response = await test_app.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    get_response = await test_app.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
