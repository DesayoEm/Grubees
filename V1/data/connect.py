from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url='postgresql://postgres:password@localhost:5432/grubees'
engine= create_engine(db_url)

with engine.connect() as connection:
    result= connection.execute(text("select 'Hello'"))

    print (result.all())



