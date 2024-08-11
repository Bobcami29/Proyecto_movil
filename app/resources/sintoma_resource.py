from flask import request, jsonify
from flask_restful import Resource
from app.models.sintoma import Sintoma
from app.extensions import db
from datetime import datetime

class SintomaResource(Resource):
    def get(self, sintoma_id=None):
        if sintoma_id:
            sintoma = Sintoma.query.get_or_404(sintoma_id)
            return jsonify(sintoma.to_dict())
        sintomas = Sintoma.query.all()
        return jsonify([s.to_dict() for s in sintomas])

    def post(self):
        data = request.get_json()
        nuevo_sintoma = Sintoma(
            tipo=data['tipo'],
            intensidad=data['intensidad'],
            fecha=datetime.fromisoformat(data['fecha'])
        )
        db.session.add(nuevo_sintoma)
        db.session.commit()
        return jsonify(nuevo_sintoma.to_dict()), 201

    def put(self, sintoma_id):
        sintoma = Sintoma.query.get_or_404(sintoma_id)
        data = request.get_json()
        sintoma.tipo = data.get('tipo', sintoma.tipo)
        sintoma.intensidad = data.get('intensidad', sintoma.intensidad)
        sintoma.fecha = datetime.fromisoformat(data.get('fecha', sintoma.fecha.isoformat()))
        db.session.commit()
        return jsonify(sintoma.to_dict())

    def delete(self, sintoma_id):
        sintoma = Sintoma.query.get_or_404(sintoma_id)
        db.session.delete(sintoma)
        db.session.commit()
        return '', 204