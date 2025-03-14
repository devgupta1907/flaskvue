from flask import Flask
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS
from application.config import LocalDevelopmentConfig
from application.models import db, User, Role
from flask_caching import Cache
from application.celery.celery_factory import celery_init_app
import flask_excel as excel


app = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    cache = Cache(app)
    
    migrate = Migrate(app, db)
    CORS(app)
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.cache = cache
    app.app_context().push()
    from application.resources import api
    api.init_app(app)
    return app


app = create_app()
celery_app = celery_init_app(app)

with app.app_context():
    db.create_all() 

import application.routes
import application.celery.celery_schedule

excel.init_excel(app)


if __name__ == "__main__":
    app.run()