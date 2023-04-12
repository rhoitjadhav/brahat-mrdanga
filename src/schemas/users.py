# Packages
from pydantic import BaseModel

# Modules
from .roles import Roles


class UsersSignUpSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    role: Roles


class UsersSignInSchema(BaseModel):
    username: str
    password: str
