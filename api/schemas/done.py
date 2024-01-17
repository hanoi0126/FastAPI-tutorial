from pydantic import BaseModel

class DoneResponse(BaseModel):
    id: int

    class ConfigDict:
        orm_mode = True