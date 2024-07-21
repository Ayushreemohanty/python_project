from flask import Flask
from .Config import Config
from .routes import employees_bp
from .db_instance import db 
from .errors import errors

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(employees_bp, url_prefix='/api')
    app.register_blueprint(errors)

    return app
