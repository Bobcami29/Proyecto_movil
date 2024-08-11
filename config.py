import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://cami:aJgwzG0CWYPjuWIPxkWlyHsN7d5S64tm@dpg-cqs26l3qf0us738skfgg-a/calendario_cbix')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False