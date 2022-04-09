from venv import create
from .api import create_app

app, db = create_app()
