from flask import Blueprint, request, jsonify
from app.models import Candidat, Competence, db

candidat_bp = Blueprint('candidat', __name__)

@candidat_bp.route('/candidats', methods=['POST'])
def add_candidat():
    data = request.get_json()
    try:
        # Crée un nouvel candidat
        new_candidat = Candidat(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            cv=data['cv'],  # Assurez-vous de gérer le fichier CV de manière appropriée
            lettreMotivation=data['lettreMotivation'],  # Assurez-vous de gérer le fichier
            experience=data['experience'],
            diplome=data['diplome'],
            categorie=data['categorie']
        )

        # Gérer les compétences
        for competence_name in data.get('competences', []):
            competence = Competence.query.filter_by(nomCompetence=competence_name).first()
            if competence is None:
                # Si la compétence n'existe pas, crée-la
                competence = Competence(nomCompetence=competence_name)
                db.session.add(competence)
            new_candidat.competences.append(competence)

        db.session.add(new_candidat)
        db.session.commit()
        return jsonify({'message': 'Candidat ajouté avec succès!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@candidat_bp.route('/candidats', methods=['GET'])
def get_candidats():
    candidats = Candidat.query.all()
    return jsonify([candidat.to_dict() for candidat in candidats]), 200  # Assurez-vous d'ajouter la méthode to_dict() dans Candidat

@candidat_bp.route('/candidats/<int:candidat_id>', methods=['GET'])
def get_candidat(candidat_id):
    candidat = Candidat.query.get(candidat_id)
    if not candidat:
        return jsonify({'error': 'Candidat non trouvé!'}), 404
    return jsonify(candidat.to_dict()), 200

@candidat_bp.route('/candidats/<int:candidat_id>', methods=['PUT'])
def update_candidat(candidat_id):
    data = request.get_json()
    candidat = Candidat.query.get(candidat_id)
    if not candidat:
        return jsonify({'error': 'Candidat non trouvé!'}), 404
    
    try:
        candidat.nom = data.get('nom', candidat.nom)
        candidat.prenom = data.get('prenom', candidat.prenom)
        candidat.email = data.get('email', candidat.email)
        # Gestion des fichiers CV et lettre de motivation ici, si nécessaire
        db.session.commit()
        return jsonify({'message': 'Candidat mis à jour avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@candidat_bp.route('/candidats/<int:candidat_id>', methods=['DELETE'])
def delete_candidat(candidat_id):
    candidat = Candidat.query.get(candidat_id)
    if not candidat:
        return jsonify({'error': 'Candidat non trouvé!'}), 404

    try:
        db.session.delete(candidat)
        db.session.commit()
        return jsonify({'message': 'Candidat supprimé avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
