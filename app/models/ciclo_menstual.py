from app.extensions import db
from datetime import datetime

class CicloMenstrual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime)
    duracion_ciclo = db.Column(db.Integer) 
    duracion_menstruacion = db.Column(db.Integer) 
    def to_dict(self):
        return {
            'id': self.id,
            'fecha_inicio': self.fecha_inicio.isoformat(),
            'fecha_fin': self.fecha_fin.isoformat() if self.fecha_fin else None,
            'duracion_ciclo': self.duracion_ciclo,
            'duracion_menstruacion': self.duracion_menstruacion
        }