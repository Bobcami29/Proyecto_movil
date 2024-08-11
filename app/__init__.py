from flask import Flask
from .extensions import db, api
from config import Config
from flask_restful import Resource
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    db.init_app(app)
    api.init_app(app)

    from .routes import init_app as init_routes
    init_routes(app)

    with app.app_context():
        db.create_all()

    print(app.url_map)
    # Imprimir rutas registradas
    for rule in app.url_map.iter_rules():
        print(f"Endpoint: {rule.endpoint}, URL: {rule}")

    return app