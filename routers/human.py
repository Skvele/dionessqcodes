from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    name: str


users = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob"),
    User(id=3, name="Bobi")
]


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users", response_model=User)
async def add_user(user: User):
    users.append(user)
    return user


@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        users.remove(user)
        # Optionally, also remove tasks assigned to this user
        global tasks
        tasks = [task for task in tasks if task.user_id != user_id]
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
