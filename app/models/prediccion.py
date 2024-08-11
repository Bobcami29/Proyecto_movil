from app.extensions import db
from datetime import datetime

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio_prediccion = db.Column(db.DateTime, nullable=False)
    fecha_fin_prediccion = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Por ejemplo: "menstruación", "ovulación", etc.

    def to_dict(self):
        return {
            'id': self.id,
            'fecha_inicio_prediccion': self.fecha_inicio_prediccion.isoformat(),
            'fecha_fin_prediccion': self.fecha_fin_prediccion.isoformat(),
            'tipo': self.tipo
        }