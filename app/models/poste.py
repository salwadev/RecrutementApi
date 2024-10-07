from app import db

class Poste(db.Model):
    __tablename__ = 'poste'
    
    idPoste = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    missions = db.Column(db.String(500), nullable=False)
    diplomes = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    salaire = db.Column(db.Float, nullable=False)
    localisation = db.Column(db.String(100), nullable=False)
    typeContrat = db.Column(db.String(50), nullable=False)

    # Relation avec Competence
    competences = db.relationship('Competence', back_populates='poste', lazy=True)

    def afficherDetails(self):
        return {
            "idPoste": self.idPoste,
            "titre": self.titre,
            "missions": self.missions,
            "competences": [competence.nomCompetence for competence in self.competences],
            "diplomes": self.diplomes,
            "experience": self.experience,
            "salaire": self.salaire,
            "localisation": self.localisation,
            "typeContrat": self.typeContrat
        }
