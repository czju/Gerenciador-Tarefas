from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.services.task_service import TaskService
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app.database import get_db

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse, summary="Cria uma nova tarefa", description="Cria uma nova tarefa com título, descrição e status.")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create_task(task.title, task.description, task.status)

@router.get("/tasks/", response_model=List[TaskResponse], summary="Lista todas as tarefas", description="Retorna uma lista de todas as tarefas.")
def list_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.list_tasks()

@router.get("/tasks/{task_id}", response_model=TaskResponse, summary="Obtém uma tarefa específica", description="Obtém os detalhes de uma tarefa específica pelo ID.")
def get_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    task = service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse, summary="Atualiza uma tarefa específica", description="Atualiza os detalhes de uma tarefa específica pelo ID.")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.update_task(task_id, task.dict())

@router.delete("/tasks/{task_id}", summary="Deleta uma tarefa específica", description="Deleta uma tarefa específica pelo ID.")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.delete_task(task_id)

