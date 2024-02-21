
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    comments = relationship("Comment", back_populates="user")

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    comment_id = Column(Integer, ForeignKey("user.id"))
    review_point = Column(Integer)

    contents = relationship("Comment", back_populates="content") # This is the relationship between the content and the comments

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("content.id"))
    comment = Column(String)

    owner = relationship("User", back_populates="comments") 

