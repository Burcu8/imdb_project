from sqlalchemy.orm import Session
from . import models, schemas


#Read a single user by ID from the database
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#Read a single user by email from the database
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#Read all users from the database
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

#Read multiple contents from the database
def get_contents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Content).offset(skip).limit(limit).all()

#Read a single content by ID from the database
def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()

