from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    Migrate(app, db)

    # Importer et enregistrer le Blueprint
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
