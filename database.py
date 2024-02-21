#import the sqlalchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a database URL 
SQLALCHEMY_DATABASE_URL = "postgresql://localhost/db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

