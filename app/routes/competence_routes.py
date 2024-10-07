from flask import Blueprint, request, jsonify
from app.models import Competence, db

competence_bp = Blueprint('competence', __name__)

@competence_bp.route('/competences', methods=['POST'])
def add_competence():
    data = request.get_json()
    try:
        new_competence = Competence(
            nomCompetence=data['nomCompetence'],
            niveau=data['niveau'],
            candidat_id=data.get('candidat_id'),
            poste_id=data.get('poste_id')
        )
        new_competence.ajouterCompetence()
        return jsonify({'message': 'Compétence ajoutée avec succès!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@competence_bp.route('/competences/<int:competence_id>', methods=['PUT'])
def update_competence(competence_id):
    data = request.get_json()
    competence = Competence.query.get(competence_id)
    if not competence:
        return jsonify({'error': 'Compétence non trouvée!'}), 404

    try:
        competence.modifierCompetence(data['nomCompetence'], data['niveau'])
        return jsonify({'message': 'Compétence mise à jour avec succès!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
