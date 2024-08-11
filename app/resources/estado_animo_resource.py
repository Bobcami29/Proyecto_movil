from flask import request
from flask_restful import Resource
from app.models.estado_animo import EstadoAnimo
from app.extensions import db
from datetime import datetime

class EstadoAnimoResource(Resource):
    def get(self, estado_id=None):
        if estado_id:
            estado = EstadoAnimo.query.get_or_404(estado_id)
            return estado.to_dict()
        estados = EstadoAnimo.query.all()
        return [e.to_dict() for e in estados]

    def post(self):
        data = request.get_json()
        nuevo_estado = EstadoAnimo(
            tipo=data['tipo'],
            fecha=datetime.fromisoformat(data['fecha'])
        )
        db.session.add(nuevo_estado)
        db.session.commit()
        return nuevo_estado.to_dict(), 201

    def put(self, estado_id):
        estado = EstadoAnimo.query.get_or_404(estado_id)
        data = request.get_json()
        estado.tipo = data.get('tipo', estado.tipo)
        estado.fecha = datetime.fromisoformat(data.get('fecha', estado.fecha.isoformat()))
        db.session.commit()
        return estado.to_dict()

    def delete(self, estado_id):
        estado = EstadoAnimo.query.get_or_404(estado_id)
        db.session.delete(estado)
        db.session.commit()
        return {'mensaje': 'Estado de ánimo eliminado exitosamente'}, 200