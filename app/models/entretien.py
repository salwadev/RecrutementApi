from app import db
class Entretien(db.Model):
    __tablename__ = 'entretien'
    
    idEntretien = db.Column(db.Integer, primary_key=True)
    dateEntretien = db.Column(db.Date, nullable=False)
    noteEntretien = db.Column(db.PickleType)  # Utilisation d'un dictionnaire pour stocker les notes par critère
    candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.idCandidat'), nullable=False)
    candidat = db.relationship('Candidat', backref='entretiens', lazy=True)
    postEntretienNotes = db.Column(db.String(500), nullable=True)

    def ajouterNotes(self, notes):
        self.noteEntretien = notes
        db.session.commit()
