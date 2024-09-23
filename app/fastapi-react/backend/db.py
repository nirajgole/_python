from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
password = 'root'
database = 'test'
port = '3306'

# creates database engine
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@localhost:{port}/{database}')

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

