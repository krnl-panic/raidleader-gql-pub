import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .gqlmodel import GQLModel

load_dotenv()  # take environment variables from .env.


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app, model_class=GQLModel)

    @app.route("/")
    def hello():
        """ """
        return "NothingToSeeHere"

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()
        result = {}
        success = True
        status_code = 200 if success else 400
        return jsonify(result), status_code

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app, db
