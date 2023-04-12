# Packages
from typing import Union
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, Response, Header, Request

# Modules
from utils.helper import Helper
from models.users import UsersModel
from db.postgres_db import get_db
from usecases.users import UsersUsecase
from schemas.users import UsersSignInSchema, UsersSignUpSchema

router = APIRouter(prefix="/users")


@router.post("/sign-in")
async def sign_in(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
        users_usecase: UsersUsecase = Depends(UsersUsecase),
):
    user = UsersSignInSchema(username=form_data.username,
                             password=form_data.password)
    result = users_usecase.sign_in(db, user, UsersModel)
    response.status_code = result.http_code

    result_dict = result.to_dict()
    result_dict.update(result_dict["data"])
    result_dict["data"] = []

    return result_dict


@router.post("/sign-up")
async def sign_up(
        user: UsersSignUpSchema,
        response: Response,
        db: Session = Depends(get_db),
        users_usecase: UsersUsecase = Depends(UsersUsecase),
):
    result = users_usecase.sign_up(db, user, UsersModel)
    response.status_code = result.http_code
    return result
