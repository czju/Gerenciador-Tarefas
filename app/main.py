from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import task_controller

app = FastAPI(
    title="Task Management API",
    description="API para gerenciamento de tarefas, permitindo criar, ler, atualizar e excluir tarefas.",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(task_controller.router, tags=["Tasks"])
