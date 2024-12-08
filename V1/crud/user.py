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