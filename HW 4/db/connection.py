from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///my_database.db")

Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()