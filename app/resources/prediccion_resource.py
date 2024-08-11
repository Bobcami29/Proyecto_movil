from flask import request, jsonify
from flask_restful import Resource
from app.models.prediccion import Prediccion
from app.extensions import db
from datetime import datetime

class PrediccionResource(Resource):
    def get(self, prediccion_id=None):
        if prediccion_id:
            prediccion = Prediccion.query.get_or_404(prediccion_id)
            return jsonify(prediccion.to_dict())
        predicciones = Prediccion.query.all()
        return jsonify([p.to_dict() for p in predicciones])

    def post(self):
        data = request.get_json()
        nueva_prediccion = Prediccion(
            fecha_inicio_prediccion=datetime.fromisoformat(data['fecha_inicio_prediccion']),
            fecha_fin_prediccion=datetime.fromisoformat(data['fecha_fin_prediccion']),
            tipo=data['tipo']
        )
        db.session.add(nueva_prediccion)
        db.session.commit()
        return jsonify(nueva_prediccion.to_dict()), 201

    def put(self, prediccion_id):
        prediccion = Prediccion.query.get_or_404(prediccion_id)
        data = request.get_json()
        prediccion.fecha_inicio_prediccion = datetime.fromisoformat(data.get('fecha_inicio_prediccion', prediccion.fecha_inicio_prediccion.isoformat()))
        prediccion.fecha_fin_prediccion = datetime.fromisoformat(data.get('fecha_fin_prediccion', prediccion.fecha_fin_prediccion.isoformat()))
        prediccion.tipo = data.get('tipo', prediccion.tipo)
        db.session.commit()
        return jsonify(prediccion.to_dict())

    def delete(self, prediccion_id):
        prediccion = Prediccion.query.get_or_404(prediccion_id)
        db.session.delete(prediccion)
        db.session.commit()
        return '', 204