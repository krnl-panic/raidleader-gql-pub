import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .gqlmodel import GQLModel

load_dotenv()  # take environment variables from .env.


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app, model_class=GQLModel)


@app.route("/")
def hello():
    """ """
    return "NothingToSeeHere"
