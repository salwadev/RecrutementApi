from app import db
class Critere(db.Model):
    __tablename__ = 'critere'
    
    idCritere = db.Column(db.Integer, primary_key=True)
    nomCritere = db.Column(db.String(100), nullable=False)  # Diplôme, Expérience, Compétence
    poidsCritere = db.Column(db.Float, nullable=False)  # Pondération

    def definirPoids(self, nouveau_poids):
        self.poidsCritere = nouveau_poids
        db.session.commit()
