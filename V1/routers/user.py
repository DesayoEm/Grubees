from fastapi import APIRouter
from crud.user import user_crud

user_router = APIRouter()

@user_router.post("/auth/register")
def register_user(db):
    pass
    # /auth/register

@user_router.post("/auth/login")
def user_login(db):
    pass
    #  /auth/login

@user_router.post("/auth/login")
def verify_email(db):
    pass
    #auth/verify-email

@user_router.get("/users/")
def search_user(db):
    pass
    #GET /api/v1/users?search=username&page=1&limit=20

@user_router.get("/users/profile")
def get_user_profile(db):
    # get profile
    pass


@user_router.get("/users/profile/posts")
def get_user_posts(db):
    # get posts
    pass


@user_router.put("/users/profile")
def update_user_profile():
    pass
    #to update bio and profile pic

@user_router.patch("/users/profile")
def patch_user_profile(db):
    pass
    #partially update bio and profile pic

@user_router.delete("/users/profile")
def delete_user(db):
    pass
