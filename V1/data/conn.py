from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

db_url='postgresql://postgres:password@localhost:5432/grubees'
engine= create_engine(db_url, echo=True)

Session=sessionmaker(bind=engine)
session = Session()

with engine.connect() as connection:
    result= connection.execute(text("select 'Hello'"))

    print (result.all())


# from sqlalchemy import inspect
# inspector = inspect(engine)
# print()
# print()
# print()
# print(inspector.get_table_names())
#
# # Method 3: If you want to see table details too:
# for table_name in inspector.get_table_names():
#     print(f"\nTable: {table_name}")
#     for column in inspector.get_columns(table_name):
#         print(f"Column: {column['name']}, Type: {column['type']}")


