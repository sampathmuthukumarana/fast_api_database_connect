from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import settings

engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600,
)

    # Test connection
# with engine.connect() as connection:
#     connection.execute(text("select 1"))
#
# print("connection is successful|")

sessionLocal= sessionmaker (bind=engine, autoflush=False, expire_on_commit=True)

class Base(DeclarativeBase):
    """base class that creates from DeclarativeBase"""


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



