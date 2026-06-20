#this file contains all the database connections and session creations 
from dotenv import load_dotenv#to import the environmental variables
import os
import psycopg2
from sqlalchemy.orm import sessionmaker,declarative_base#to create session and to recognize the classes as tables
from sqlalchemy import create_engine#to create a connection to database
load_dotenv()
#let's fetch the url of the database
DATABASE_URL=os.getenv('DATABASE_URL')
#let's create a base for all the tables
Base=declarative_base()
#let's connect the database
engine=create_engine(DATABASE_URL)
#let's create a session 
SessionLocal=sessionmaker(bind=engine)