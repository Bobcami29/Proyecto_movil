from app.extensions import db
from datetime import datetime

class EstadoAnimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'fecha': self.fecha.isoformat()
        }