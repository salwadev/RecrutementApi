from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crée une instance de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Remplace par ton chemin de config
    db.init_app(app)  # Initialise SQLAlchemy avec l'application

    with app.app_context():
        # Importer les modèles ici après l'initialisation
      # Importation des modèles ici
        from .candidat import Candidat  # Assurez-vous que le chemin est correct
        from .competence import Competence
        from .modele_ml import ModeleML
        from .analyse_recrutement import AnalyseRecrutement
        from .poste import Poste
        from .entretien import Entretien
        from .critere import Critere
        
        db.create_all()  # Crée toutes les tables définies par les modèles

    return app
