from flask import Blueprint, request, jsonify
from app.models import Poste, db

poste_bp = Blueprint('poste', __name__)

@poste_bp.route('/postes', methods=['POST'])
def add_poste():
    data = request.get_json()
    try:
        new_poste = Poste(
            titre=data['titre'],
            missions=data['missions'],
            competences=data.get('competences', []),
            diplome=data['diplome'],
            experience=data['experience'],
            salaire=data['salaire'],
            localisation=data['localisation'],
            typeContrat=data['typeContrat']
        )
        db.session.add(new_poste)
        db.session.commit()
        return jsonify({'message': 'Poste ajouté avec succès!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@poste_bp.route('/postes', methods=['GET'])
def get_postes():
    postes = Poste.query.all()
    return jsonify([poste.to_dict() for poste in postes]), 200  # Ajoute la méthode to_dict() dans Poste

@poste_bp.route('/postes/<int:poste_id>', methods=['GET'])
def get_poste(poste_id):
    poste = Poste.query.get(poste_id)
    if not poste:
        return jsonify({'error': 'Poste non trouvé!'}), 404
    return jsonify(poste.to_dict()), 200

@poste_bp.route('/postes/<int:poste_id>', methods=['PUT'])
def update_poste(poste_id):
    data = request.get_json()
    poste = Poste.query.get(poste_id)
    if not poste:
        return jsonify({'error': 'Poste non trouvé!'}), 404

    try:
        poste.titre = data.get('titre', poste.titre)
        poste.missions = data.get('missions', poste.missions)
        poste.competences = data.get('competences', poste.competences)
        poste.diplome = data.get('diplome', poste.diplome)
        poste.experience = data.get('experience', poste.experience)
        poste.salaire = data.get('salaire', poste.salaire)
        poste.localisation = data.get('localisation', poste.localisation)
        poste.typeContrat = data.get('typeContrat', poste.typeContrat)
        
        db.session.commit()
        return jsonify({'message': 'Poste mis à jour avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@poste_bp.route('/postes/<int:poste_id>', methods=['DELETE'])
def delete_poste(poste_id):
    poste = Poste.query.get(poste_id)
    if not poste:
        return jsonify({'error': 'Poste non trouvé!'}), 404

    try:
        db.session.delete(poste)
        db.session.commit()
        return jsonify({'message': 'Poste supprimé avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
