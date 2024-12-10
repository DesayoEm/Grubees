from V1.models.user import Base, User
from conn import engine

Base.metadata.create_all(bind=engine)

# for table_name, table in Base.metadata.tables.items():
#     print(f"Table name: {table_name}")
#     print(f"Columns: {table.columns.keys()}")


# from sqlalchemy import text
# with engine.connect() as conn:
#     result = conn.execute(text("""
#         SELECT table_name, column_name, data_type
#         FROM information_schema.columns
#         WHERE table_schema = 'public'
#         ORDER BY table_name, ordinal_position
#     """))
#     for row in result:
#         print(row)
