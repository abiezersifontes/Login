from dataclasses import asdict
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.api.schemas import SignInRequest, SignOutRequest, CreateUserRequest
from app.domain.services import AuthService, UserService
from app.domain.repositories import AbstractUserRepository
from app.infrastructure.repositories import SqlAlchemyUserRepository
from app.infrastructure.database import SessionLocal

user_router = APIRouter()


def get_user_repository() -> AbstractUserRepository:
    return SqlAlchemyUserRepository(SessionLocal())

@user_router.post("/user")
async def create_user(
    create_user_request: CreateUserRequest, 
    user_repository: AbstractUserRepository = Depends(get_user_repository)
):
    user_service = UserService(user_repository)
    
    if not user_service.is_unique(create_user_request.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return JSONResponse(
        asdict(
            user_service.create_user(**create_user_request.dict())
        ),
        201
    )

@user_router.post("/signin")
async def sign_in(sign_in_request: SignInRequest, user_repository: AbstractUserRepository = Depends(get_user_repository)):
    auth_service = AuthService(user_repository)
    token = auth_service.sign_in(sign_in_request.username, sign_in_request.password)
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": token}


@user_router.post("/signout")
async def sign_out(sign_out_request: SignOutRequest, user_repository: AbstractUserRepository = Depends(get_user_repository)):
    auth_service = AuthService(user_repository)
    auth_service.sign_out(sign_out_request.username)
    return {"message": "Successfully signed out"}
