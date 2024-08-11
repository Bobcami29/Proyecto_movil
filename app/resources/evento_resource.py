from flask import request
from flask_restful import Resource
from app.models.evento import Evento
from app.extensions import db
from datetime import datetime

class EventoResource(Resource):
    def get(self, evento_id=None):
        if evento_id:
            evento = Evento.query.get_or_404(evento_id)
            return evento.to_dict()
        eventos = Evento.query.all()
        return [e.to_dict() for e in eventos]

    def post(self):
        data = request.get_json()
        nuevo_evento = Evento(
            titulo=data['titulo'],
            descripcion=data.get('descripcion'),
            fecha=datetime.fromisoformat(data['fecha']),
            hora_inicio=datetime.fromisoformat(data['hora_inicio']).time() if data.get('hora_inicio') else None,
            hora_fin=datetime.fromisoformat(data['hora_fin']).time() if data.get('hora_fin') else None,
            tipo=data.get('tipo'),
            recordatorio=data.get('recordatorio'),
            repeticion=data.get('repeticion')
        )
        db.session.add(nuevo_evento)
        db.session.commit()
        return nuevo_evento.to_dict(), 201

    def put(self, evento_id):
        evento = Evento.query.get_or_404(evento_id)
        data = request.get_json()
        evento.titulo = data.get('titulo', evento.titulo)
        evento.descripcion = data.get('descripcion', evento.descripcion)
        evento.fecha = datetime.fromisoformat(data.get('fecha', evento.fecha.isoformat()))
        evento.hora_inicio = datetime.fromisoformat(data['hora_inicio']).time() if data.get('hora_inicio') else evento.hora_inicio
        evento.hora_fin = datetime.fromisoformat(data['hora_fin']).time() if data.get('hora_fin') else evento.hora_fin
        evento.tipo = data.get('tipo', evento.tipo)
        evento.recordatorio = data.get('recordatorio', evento.recordatorio)
        evento.repeticion = data.get('repeticion', evento.repeticion)
        db.session.commit()
        return evento.to_dict()

    def delete(self, evento_id):
        evento = Evento.query.get_or_404(evento_id)
        db.session.delete(evento)
        db.session.commit()
        return {'mensaje': 'Evento eliminado exitosamente'}, 200