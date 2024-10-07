from app import db

class Competence(db.Model):
    __tablename__ = 'competence'
    
    idCompetence = db.Column(db.Integer, primary_key=True)
    nomCompetence = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.Integer, nullable=False)  # Niveau de 1 à 5
    candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.idCandidat'), nullable=True)
    poste_id = db.Column(db.Integer, db.ForeignKey('poste.idPoste'), nullable=True)

    # Relation avec Poste
    poste = db.relationship('Poste', back_populates='competences', lazy=True)

    def ajouterCompetence(self):
        db.session.add(self)
        db.session.commit()

    def modifierCompetence(self, nomCompetence, niveau):
        self.nomCompetence = nomCompetence
        self.niveau = niveau
        db.session.commit()
