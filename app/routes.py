from app.extensions import Api
from app.resources.evento_resource import EventoResource
from app.resources.ciclo_menstrual_resource import CicloMenstrualResource
from app.resources.sintoma_resource import SintomaResource
from app.resources.estado_animo_resource import EstadoAnimoResource
from app.resources.medicamento__resource import MedicamentoResource
from app.resources.prediccion_resource import PrediccionResource
from flask import jsonify

def init_app(app):
    api = Api(app)
    
    api.add_resource(EventoResource, '/eventos', '/eventos/<int:evento_id>')      
    api.add_resource(CicloMenstrualResource, '/ciclos', '/ciclos/<int:ciclo_id>')
    api.add_resource(SintomaResource, '/sintomas', '/sintomas/<int:sintoma_id>')
    api.add_resource(EstadoAnimoResource, '/estados-animo', '/estados-animo/<int:estado_animo_id>')
    api.add_resource(MedicamentoResource, '/medicamentos', '/medicamentos/<int:medicamento_id>')
    api.add_resource(PrediccionResource, '/predicciones', '/predicciones/<int:prediccion_id>')
