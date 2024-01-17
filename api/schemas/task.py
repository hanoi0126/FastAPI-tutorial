from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, examples=["Pytorchの勉強をする"])

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
    class ConfigDict:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class ConfigDict:
        orm_mode = True
