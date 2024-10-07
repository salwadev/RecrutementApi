from flask import Blueprint, request, jsonify
from app.models import Entretien, db

entretien_bp = Blueprint('entretien', __name__)

@entretien_bp.route('/entretiens', methods=['POST'])
def add_entretien():
    data = request.get_json()
    try:
        new_entretien = Entretien(
            dateEntretien=data['dateEntretien'],
            noteEntretien=data['noteEntretien'],
            candidat_id=data['candidat_id'],  # Associe le candidat
            postEntretienNotes=data['postEntretienNotes']
        )
        db.session.add(new_entretien)
        db.session.commit()
        return jsonify({'message': 'Entretien ajouté avec succès!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@entretien_bp.route('/entretiens', methods=['GET'])
def get_entretiens():
    entretiens = Entretien.query.all()
    return jsonify([entretien.to_dict() for entretien in entretiens]), 200  # Ajoute la méthode to_dict() dans Entretien

@entretien_bp.route('/entretiens/<int:entretien_id>', methods=['GET'])
def get_entretien(entretien_id):
    entretien = Entretien.query.get(entretien_id)
    if not entretien:
        return jsonify({'error': 'Entretien non trouvé!'}), 404
    return jsonify(entretien.to_dict()), 200

@entretien_bp.route('/entretiens/<int:entretien_id>', methods=['PUT'])
def update_entretien(entretien_id):
    data = request.get_json()
    entretien = Entretien.query.get(entretien_id)
    if not entretien:
        return jsonify({'error': 'Entretien non trouvé!'}), 404

    try:
        entretien.dateEntretien = data.get('dateEntretien', entretien.dateEntretien)
        entretien.noteEntretien = data.get('noteEntretien', entretien.noteEntretien)
        entretien.postEntretienNotes = data.get('postEntretienNotes', entretien.postEntretienNotes)

        db.session.commit()
        return jsonify({'message': 'Entretien mis à jour avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@entretien_bp.route('/entretiens/<int:entretien_id>', methods=['DELETE'])
def delete_entretien(entretien_id):
    entretien = Entretien.query.get(entretien_id)
    if not entretien:
        return jsonify({'error': 'Entretien non trouvé!'}), 404

    try:
        db.session.delete(entretien)
        db.session.commit()
        return jsonify({'message': 'Entretien supprimé avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
