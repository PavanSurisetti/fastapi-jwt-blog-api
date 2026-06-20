#this file contains all the models that we use in the Blog API
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship#this is used to maintain the relationship 
from sqlalchemy import Column,Integer,String,ForeignKey,Text,DateTime
#these are used to column with datatypes Integer,and also adds a foreign key constraint

#---let's create a first model----
#user model
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)#this is the id of the user which is unique 
    name=Column(String,nullable=False)#this is the name of the user
    email=Column(String,unique=True,nullable=False)#this is the email of the user
    password=Column(String,nullable=False)#this is the password for the account
    post=relationship('Post',back_populates='owner')
#----let's create a second table----
#post table
class Post(Base):
    __tablename__='post'
    id=Column(Integer,primary_key=True)#this is the post id which is unique
    title=Column(String,nullable=False)#this is the post title and it cannot be null
    content=Column(Text,nullable=False)#this is the actual content of the post
    created_at=Column(DateTime,nullable=False,default=datetime.utcnow())#this is the date of the post 
    owner_id=Column(Integer,ForeignKey("user.id"))
    owner=relationship('User',back_populates='post')