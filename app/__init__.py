from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.bootstrap import Bootstrap
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


lm = LoginManager()
lm.session_protection = 'strong'

# create app
app = Flask(__name__)
app.config.from_object('config')

# initialise db
db = SQLAlchemy(app)
from app import views, models

# initialise Twitter Bootstrap
bootstrap = Bootstrap(app)

# initialise migration tool
migrate = Migrate(app, db)

# initialise cli-parser
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# initialise login manager
lm.init_app(app)
lm.login_view = 'login'



