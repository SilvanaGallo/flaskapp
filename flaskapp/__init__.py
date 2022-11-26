import os
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskapp.config import Config
from flaskapp.main.repository import RollbarRepository

db = SQLAlchemy()
migrate = Migrate(db, compare_type=True) 
repository = RollbarRepository()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    from flaskapp.main.routes import main
    from flaskapp.items.routes import items
    app.register_blueprint(main)
    app.register_blueprint(items)

    return app
