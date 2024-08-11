from flask import request
from flask_restful import Resource
from app.models.medicamento import Medicamento
from app.extensions import db

class MedicamentoResource(Resource):
    def get(self, medicamento_id=None):
        if medicamento_id:
            medicamento = Medicamento.query.get_or_404(medicamento_id)
            return medicamento.to_dict()
        medicamentos = Medicamento.query.all()
        return [m.to_dict() for m in medicamentos]

    def post(self):
        data = request.get_json()
        nuevo_medicamento = Medicamento(
            nombre=data['nombre']
        )
        db.session.add(nuevo_medicamento)
        db.session.commit()
        return nuevo_medicamento.to_dict(), 201

    def put(self, medicamento_id):
        medicamento = Medicamento.query.get_or_404(medicamento_id)
        data = request.get_json()
        medicamento.nombre = data.get('nombre', medicamento.nombre)
        db.session.commit()
        return medicamento.to_dict()

    def delete(self, medicamento_id):
        medicamento = Medicamento.query.get_or_404(medicamento_id)
        db.session.delete(medicamento)
        db.session.commit()
        response.headers['X-Status-Message'] = 'Medicamento eliminado exitosamente'
        return response