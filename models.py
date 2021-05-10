## This file will set up the database models and structure for the flask API to make calls to the database.
## This file will also be used to help with the data base migrations
## It serves the prupose for creating new data tables however data tables must be updated with the manage.py file.
#from sqlalchemy import all
from app import db
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.postgresql 
import os
#This is where we create the new data base table for PSQL to take in. 
#We set up our database model here so that migrations and handling data and pushing data to the database will be easy without dealing with so much parsing. 

#app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
class Temp_Data(db.Model): # We create the database type for python to understand i
    __tablename__= "temp_data"

    id = db.Column(db.Integer,primary_key=True)
    time = db.Column(db.Integer)
    temp = db.Column(db.Integer) 

    def __init__(self,time,temp):
        self.time = time
        self.temp = temp
    
    def __repr__(self):
        return '<temp %r>' % self.temp
