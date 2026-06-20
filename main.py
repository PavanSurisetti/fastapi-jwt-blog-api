#this file conatins the endpoints of the API
from fastapi import FastAPI,Depends,HTTPException#used to create application
from database import Base,engine,SessionLocal
from datetime import datetime,timedelta
from pydantic import BaseModel#for data validation
import models
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
pwd_context=CryptContext(schemes=['bcrypt'], deprecated="auto")
from sqlalchemy.orm import Session
oauth2scheme=OAuth2PasswordBearer(tokenUrl='login')
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
#let's create all tables in the database
Base.metadata.create_all(engine)
#let's create APP
app=FastAPI()
#dependency function
def get_db():
    db=SessionLocal()
    try:
        yield db#this will db to API
    finally:
        db.close()
#--hashed verison of password
def hashPassword(password:str):
    return pwd_context.hash(password)
#--verifying hash passwrd with original password
def verifyPassword(password,hashpassword):
    return pwd_context.verify(password,hashpassword)
#--creation of token---
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
#--pydantic for registration--
class UserReistration(BaseModel):
    name:str
    email:str
    password:str
#--pydantic for creaion of post--
class postCreation(BaseModel):
    title:str
    content:str
#----pydantic for updating posts----
class UpdatePost(BaseModel):
    title:str
    content:str
#welcome message to API
@app.get('/',tags=['Welcome'])
def home():
    return {'Welcome to Blog API'}
#-----1.register user ----
@app.post('/register',tags=['Register User'])
def register(add:UserReistration,db:Session=Depends(get_db)):
    user=models.User(name=add.name,email=add.email,password=hashPassword(add.password))
    #add to session
    db.add(user)
    #commiting to db
    db.commit()
    #refreshing db
    db.refresh(user)
    return{
        'message':'user created',
        'user':user.id
    }
#-----2.Login User------
@app.post('/login',tags=['Login'])
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==form_data.username).first()
    if not user:
        raise HTTPException(status_code=404,detail='User Not Found')
    if not verifyPassword(form_data.password,user.password):
        raise HTTPException(status_code=401,detail='Invalid Credentials')
    token=create_token({'sub':str(user.id)})
    return {
        'access_token':token,
        'token_type': 'bearer'
    }
def get_current_user(token: str = Depends(oauth2scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(models.User).filter(models.User.id == int(user_id)).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid")
#-----3.create post-----
@app.post('/posts',tags=['Post Creation'])
def posts(add:postCreation,db:Session=Depends(get_db),current_user:models.User=Depends(get_current_user)):
    post=models.Post(title=add.title,content=add.content,owner_id=current_user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {
        'message':'Post Created',
        'post id':post.id
    }
#----4 GET ALL POSTS (PUBLIC)-----
@app.get('/posts',tags=['Get all posts'])
def getall(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=404,detail='Posts Not Found')
    return{
        'message':'All Posted Fetched Successfully ',
        'posts':posts
    }
#--- Get all posts private posts
@app.get('/posts/private',tags=['Private Posts'])
def private(db:Session=Depends(get_db),current_user:models.User=Depends(get_current_user)):#current_user: models.User ==> current_user will be a User object
    post=db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    if not post:
        raise HTTPException(status_code=404,detail='Posts not Found')
    return{
        'posts':post
    }
#5 get post by id
@app.get('/post/{id}',tags=['Get Post by ID'])
def postid(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=404,detail='Post Not Found')
    return{
        'post':post
    }
#---6 — UPDATE POST-----
@app.put('/posts/{id}')
def update(*,id:int,db:Session=Depends(get_db),update:UpdatePost,currentuser:models.User=Depends(get_current_user)):
    user=db.query(models.Post).filter(models.Post.owner_id==currentuser.id).first()
    if not user:
        raise HTTPException(status_code=404,detail='User Not Found')
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=404,detail='Post Not Found')
    #  ownership check (IMPORTANT)
    if post.owner_id != currentuser.id:
        raise HTTPException(status_code=403, detail='Not allowed to Update this post')
    post.title=update.title
    post.content=update.content
    db.commit()
    db.refresh(post)
    return{
        'message':'Updated successfully',
        'post':post
    }
#----7-delete post-----
@app.delete('/posts/{id}')
def deletePosts(id: int,db: Session = Depends(get_db),current_user: models.User = Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post Not Found')
    #  ownership check (IMPORTANT)
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail='Not allowed to delete this post')
    db.delete(post)
    db.commit()
    return {
        'message': 'Deleted Successfully'
    }