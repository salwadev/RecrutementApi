from flask import Flask 
from app.config import Config
from app.models import db
from app.routes.candidat_routes import candidat_bp
from app.routes.poste_routes import poste_bp
from app.routes.competence_routes import competence_bp  # Assure-toi d'importer le blueprint ici

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Enregistrement des Blueprints
app.register_blueprint(candidat_bp)
app.register_blueprint(poste_bp)
app.register_blueprint(competence_bp)  # Enregistre le blueprint des compétences ici

@app.before_first_request
def create_tables():
    db.create_all()  # Crée toutes les tables définies par les modèles

if __name__ == '__main__':
    app.run(debug=True)  
