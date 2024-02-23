from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url_db = 'sqlite:///./db_app.db'

engine = create_engine(url_db, connect_args = {'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)


Base = declarative_base()