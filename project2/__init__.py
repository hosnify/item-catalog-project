from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
from project2.config import Config
import os

app = Flask(__name__)
db=SQLAlchemy()
marshmallow = Marshmallow()
bcrypt = Bcrypt()
login_manager=LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
Base = declarative_base()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    db.init_app(app)
    marshmallow.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from project2.users.views import users ,google_blueprint
    from project2.categories.views import categories
    from project2.courses.views import courses
    from project2.main.views import main
    from project2.errors.errorhandlers import errorhandlers
    app.register_blueprint(users)
    app.register_blueprint(categories)
    app.register_blueprint(courses)
    app.register_blueprint(main)
    app.register_blueprint(errorhandlers)
    app.register_blueprint(google_blueprint, url_prefix="/login")

    return app
create_app().app_context().push()