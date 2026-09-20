from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(settings.database_url)

with engine.connect() as connection:
    connection.execute(text("select 1"))

print("connection is successful|")

# test commit