from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Task(BaseModel):
    id: int
    name: str
    completed: bool = False
    user_id: Optional[int] = None


# Initial data
tasks = [
    Task(id=1, name="jump", user_id=1),
    Task(id=2, name="run", user_id=2),
    Task(id=3, name="swim", user_id=3)
]


@router.get("/tasks", response_model=List[Task])
def get_tasks(user_id: Optional[int] = None):
    if user_id is not None:
        return [task for task in tasks if task.user_id == user_id]
    return tasks


@router.post("/tasks", response_model=Task)
def add_task(task: Task):
    tasks.append(task)
    return task


@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        tasks.remove(task)
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")
