from ariadne.asgi import GraphQL
from fastapi.applications import FastAPI

from .context import get_graphql_context
from .database import db
from .graphql import schema


def create_app():
    """Create the FastAPI application."""
    app = FastAPI(title="GraphQL API server for raidleader.io")
    db.init_app(app)

    app.mount(
        "/graphql",
        GraphQL(schema=schema, debug=True, context_value=get_graphql_context),
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    return app
