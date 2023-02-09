from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, mapper
from settings.config import load_env_config
from datetime import datetime, date, timedelta
import urllib.parse

config = load_env_config()


quoted = urllib.parse.quote_plus(config['database_string'])

SQLALCHEMY_DATABASE_URL  = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=60)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

session = SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()


def create_customised_datetime():
    today = datetime.now()
    date_time = today.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time

