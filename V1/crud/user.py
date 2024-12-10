import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import Base, User
from conn import engine

Base.metadata.create_all(bind=engine)



current_file = os.path.abspath(__file__)
print(f"Current file location: {current_file}")


current_dir = os.path.dirname(current_file)
print(f"Current directory: {current_dir}")

print(sys.path)
try:
    print("\nAttempting to import models.user...")
    from models.user import Base, User
    print("import successful")
except ImportError as e:
    print(f"import failed with error: {str(e)}")

    from schemas.user import Login, NewUser, UserProfile, UserAccount,\
    UserInfo, AccountUpdate,ProfileUpdate
from uuid import UUID



class UserCrud:
    @staticmethod
    def register_user(db):
        pass
        # POST /auth/register

    @staticmethod
    def user_login(db):
        pass
        # POST /auth/login

    @staticmethod
    def verify_email(db):
        pass
        # GET /auth/verify-email

    @staticmethod
    def get_user_profile(db):
        # GET /user/profile
        pass

    @staticmethod
    def search_user(db):
        pass
        #GET /api/v1/users?search=username&page=1&limit=20

    @staticmethod
    def get_user_posts(db):
        # GET /user/profile/posts
        pass

    @staticmethod
    def update_user_profile(db):
        pass
        # PUT /user/profile (to update bio and profile pic)

    @staticmethod
    def patch_user_profile(db):
        pass
        # PUT /user/profile (to update bio and profile pic)

    @staticmethod
    def change_user_password():
        pass
        #POST /users/account/change-password


    @staticmethod
    def delete_user(db):
        pass

user_crud=UserCrud