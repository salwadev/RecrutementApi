from flask import Blueprint, request, jsonify
from app.models import AnalyseRecrutement, db

analyse_bp = Blueprint('analyse', __name__)

@analyse_bp.route('/analyses', methods=['POST'])
def add_analyse():
    data = request.get_json()
    try:
        new_analyse = AnalyseRecrutement(
            data=data['data'],
            typeAnalyse=data['typeAnalyse'],
            resultats=data['resultats']
        )
        db.session.add(new_analyse)
        db.session.commit()
        return jsonify({'message': 'Analyse ajoutée avec succès!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@analyse_bp.route('/analyses', methods=['GET'])
def get_analyses():
    analyses = AnalyseRecrutement.query.all()
    return jsonify([analyse.to_dict() for analyse in analyses]), 200  # Ajoute la méthode to_dict() dans AnalyseRecrutement

@analyse_bp.route('/analyses/<int:analyse_id>', methods=['GET'])
def get_analyse(analyse_id):
    analyse = AnalyseRecrutement.query.get(analyse_id)
    if not analyse:
        return jsonify({'error': 'Analyse non trouvée!'}), 404
    return jsonify(analyse.to_dict()), 200

@analyse_bp.route('/analyses/<int:analyse_id>', methods=['PUT'])
def update_analyse(analyse_id):
    data = request.get_json()
    analyse = AnalyseRecrutement.query.get(analyse_id)
    if not analyse:
        return jsonify({'error': 'Analyse non trouvée!'}), 404

    try:
        analyse.data = data.get('data', analyse.data)
        analyse.typeAnalyse = data.get('typeAnalyse', analyse.typeAnalyse)
        analyse.resultats = data.get('resultats', analyse.resultats)

        db.session.commit()
        return jsonify({'message': 'Analyse mise à jour avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@analyse_bp.route('/analyses/<int:analyse_id>', methods=['DELETE'])
def delete_analyse(analyse_id):
    analyse = AnalyseRecrutement.query.get(analyse_id)
    if not analyse:
        return jsonify({'error': 'Analyse non trouvée!'}), 404

    try:
        db.session.delete(analyse)
        db.session.commit()
        return jsonify({'message': 'Analyse supprimée avec succès!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
