from fastapi import FastAPI

from routers import taskss, human

app = FastAPI()

app.include_router(taskss.router)
app.include_router(human.router)
