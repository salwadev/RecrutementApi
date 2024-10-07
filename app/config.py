import os

class Config:
    # Clé secrète pour la sécurité des sessions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Configurer la base de données SQLite (pour débuter)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recruitment.db'

    # Désactiver le suivi des modifications (inutile pour notre projet)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
