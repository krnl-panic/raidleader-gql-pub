from api import app, db
from api.context import get_graphql_context

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.mutations import mutation
from api.queries import query

type_defs = load_schema_from_path('api/schema.graphql')
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
async def graphql_server():
    data = request.get_json()
    success, result = await graphql(
        schema,
        data,
        context_value=get_graphql_context(request),
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code