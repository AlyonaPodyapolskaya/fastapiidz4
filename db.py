from sqlalchemy import create_engine
from config import settings
#from sqlalchemy.ext.declarative import declarative_base

ur_s = settings.POSTGRES_DATABASE_URLS
#ur_a = settings.POSTGRES_DATABASE_URLA



#engine = create_async_engine(ur_p, echo=True)
engine_s = create_engine(ur_s, echo=True)
#Base = declarative_base(bind=engine_s)
