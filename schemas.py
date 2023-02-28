from pydantic import BaseModel


class UserBase(BaseModel):
    username: str = "TestNames"
    email: str = "Testemail@gmail.com"
    password: str = "Pass12345"


class UserDisplay(BaseModel):
    username: str = "already"
    email: str = "exist"

    class Config:
        orm_mode = True


