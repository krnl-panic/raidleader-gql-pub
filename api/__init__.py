import json
from ariadne import graphql as GraphQL
from ariadne.asgi import PLAYGROUND_HTML
from fastapi import Request, Response
from fastapi.applications import FastAPI

from .context import get_graphql_context
from .database import engine, Session
from .graphql import schema


def create_app():
    """Create the FastAPI application."""
    app = FastAPI(title="GraphQL API server for raidleader.io")

    @app.on_event("shutdown")
    async def shutdown():
        await engine.dispose()

    @app.get("/")
    def read_root(_: Request, response: Response):
        response.status_code = 401
        return response

    @app.get("/graphql")
    def graphql_playground(_request: Request, _response: Response):
        return PLAYGROUND_HTML

    @app.post("/graphql")
    async def graphql_server(request: Request, _response: Response):
        async with Session() as session:
            async with session.begin():
                data = await request.json()
                success, response = await GraphQL(
                    schema,
                    data,
                    context_value=get_graphql_context(request, session),
                    debug=True,
                )
                if success:
                    return response
                _response.status_code = 400
                session.close()
                return _response

    # app.mount(
    #     "/graphql",
    #     GraphQL(schema=schema, debug=True, context_value=get_graphql_context),
    # )

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
