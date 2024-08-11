from flask import request, jsonify
from flask_restful import Resource
from app.models.ciclo_menstual import CicloMenstrual
from app.extensions import db
from datetime import datetime

class CicloMenstrualResource(Resource):
    def get(self, ciclo_id=None):
        if ciclo_id:
            ciclo = CicloMenstrual.query.get_or_404(ciclo_id)
            return ciclo.to_dict()
        ciclos = CicloMenstrual.query.all()
        return [c.to_dict() for c in ciclos]

    def post(self):
        data = request.get_json()
        nuevo_ciclo = CicloMenstrual(
            fecha_inicio=datetime.fromisoformat(data['fecha_inicio']),
            fecha_fin=datetime.fromisoformat(data['fecha_fin']) if data.get('fecha_fin') else None,
            duracion_ciclo=data.get('duracion_ciclo'),
            duracion_menstruacion=data.get('duracion_menstruacion')
        )
        db.session.add(nuevo_ciclo)
        db.session.commit()
        return nuevo_ciclo.to_dict(), 201

    def put(self, ciclo_id):
        ciclo = CicloMenstrual.query.get_or_404(ciclo_id)
        data = request.get_json()
        ciclo.fecha_inicio = datetime.fromisoformat(data.get('fecha_inicio', ciclo.fecha_inicio.isoformat()))
        ciclo.fecha_fin = datetime.fromisoformat(data.get('fecha_fin', ciclo.fecha_fin.isoformat() if ciclo.fecha_fin else None))
        ciclo.duracion_ciclo = data.get('duracion_ciclo', ciclo.duracion_ciclo)
        ciclo.duracion_menstruacion = data.get('duracion_menstruacion', ciclo.duracion_menstruacion)
        db.session.commit()
        return ciclo.to_dict()

    def delete(self, ciclo_id):
        ciclo = CicloMenstrual.query.get_or_404(ciclo_id)
        db.session.delete(ciclo)
        db.session.commit()
        response = make_response('', 204)
        response.headers['X-Status-Message'] = 'Ciclo menstrual eliminado exitosamente'
        return response