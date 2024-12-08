from schemas.user import UserBase, User, UserUpdate
from uuid import UUID

def register_user(db):
    pass
    # POST /auth/register

def user_login(db):
    pass
    # POST /auth/login

def verify_email(db):
    pass
    # GET /auth/verify-email

def get_user_profile(db):
    # GET /user/profile
    pass

def get_user_posts(db):
    # GET /user/profile/posts
    pass

def update_user_profile(db):
    pass
    # PUT /user/profile (to update bio and profile pic)

def patch_user_profile(db):
    pass
    # PUT /user/profile (to update bio and profile pic)

def delete_user(db):
    pass

def search_user(db):
    pass
    #GET /api/v1/users?search=username&page=1&limit=20
