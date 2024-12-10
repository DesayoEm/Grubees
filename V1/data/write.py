from V1.models.user import User
from sqlalchemy.orm import Session
from V1.schemas.user_enums import GenderEnum, CountryEnum
from conn import engine
from datetime import date, datetime, UTC
from V1.models.base import Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    user1 = User(
        username="Kefee",
        email_address="kefee20@gmail.com",
        password="password",
        full_name="Kefee Alabi",
        date_of_birth=date(2000, 10, 20),
        bio="Foodie, reader",
        gender=GenderEnum.Female,
        phone="12345667888",
        country=CountryEnum.GHANA,
        is_active=False,
        is_verified=False,
        is_public=True
    )
    session.add(user1)
    session.commit()