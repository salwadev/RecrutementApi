# app/models/candidat.py

from app import db

class Candidat(db.Model):
    __tablename__ = 'candidat'

    idCandidat = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    cv = db.Column(db.String(200), nullable=False)  # Stocke le chemin du fichier CV
    lettreMotivation = db.Column(db.String(200), nullable=False)  # Stocke le chemin du fichier
    competences = db.relationship('Competence', backref='candidat', lazy=True)
    experience = db.Column(db.Integer, nullable=False)
    diplome = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(50), nullable=True)  # Sérieux, Pourquoi pas, À écarter

    def soumettreCandidature(self):
        return {
            "idCandidat": self.idCandidat,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "cv": self.cv,
            "lettreMotivation": self.lettreMotivation,
            "competences": [competence.nomCompetence for competence in self.competences],
            "experience": self.experience,
            "diplome": self.diplome,
            "categorie": self.categorie
        }
