from pydantic import BaseModel


class IdentitySchema(BaseModel):
    id: int
