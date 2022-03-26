from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.mutations import create_raid_resolver, delete_raid_resolver, update_raid_resolver
from api.queries import listRaids_resolver, getRaid_resolver

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

query = ObjectType("Query")
mutation = ObjectType("Mutation")
query.set_field("listRaids", listRaids_resolver)
query.set_field("getRaid", getRaid_resolver)
mutation.set_field("createRaid", create_raid_resolver)
mutation.set_field("updateRaid", update_raid_resolver)
mutation.set_field("deleteRaid", delete_raid_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code