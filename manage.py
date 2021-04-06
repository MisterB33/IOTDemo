import os 
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand 
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import alembic_script

from app import app, db 
import sqlalchemy
app.config.from_object(os.environ['APP_SETTINGS'])
#createing data base migration by getting data base connection from the app 
migrate = Migrate(app,db) 
#ininitializing and connecting nmanager client to our app
manager = Manager(app) 
#adding the db command to intialize and hand the database migration to be handled by Alembic
manager.add_command('db',MigrateCommand) 

if __name__== '__main__':
    manager.run() 
