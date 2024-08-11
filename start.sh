#!/bin/bash

flask db upgrade

python << END
from run import create_app
from app import db

app = create_app()
with app.app_context():
    db.create_all()
END

gunicorn "run:create_app()"