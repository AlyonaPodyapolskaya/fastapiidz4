from sqlalchemy import create_engine
from config import settings
from sqlalchemy.ext.declarative import declarative_base

ur_s = settings.POSTGRES_DATABASE_URLS



print(ur_s)

engine_s = create_engine(ur_s, echo=True)
Base = declarative_base(bind=engine_s)



def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)


