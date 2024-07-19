from app.models.greeting import Greet
from flask_restx import Namespace, Resource, fields

greet_ns = Namespace("greet", description="Greet related operations")

greet_model = greet_ns.model(
    "Greet",
    {
        "id": fields.Integer(readOnly=True, description="The greeting identifier"),
        "msg": fields.String(required=True, description="The greeting message"),
    },
)


@greet_ns.route("/")
class GreetList(Resource):
    @greet_ns.doc("list_greetings")
    @greet_ns.marshal_list_with(greet_model)
    def get(self):
        """List all greetings"""
        return Greet.query.all()

    @greet_ns.doc("create_greeting")
    @greet_ns.expect(greet_model)
    @greet_ns.marshal_with(greet_model, code=201)
    def post(self):
        """Create a new greeting"""
        data = greet_ns.payload
        greeting = Greet(msg=data["msg"])
        greeting.save()
        return greeting, 201


@greet_ns.route("/<int:id>")
class GreetResource(Resource):
    @greet_ns.doc("get_greeting")
    @greet_ns.marshal_with(greet_model)
    def get(self, id):
        """Get a greeting by ID"""
        return Greet.query.get_or_404(id)

    @greet_ns.doc("delete_greeting")
    @greet_ns.response(204, "Greeting deleted")
    def delete(self, id):
        """Delete a greeting by ID"""
        greeting = Greet.query.get_or_404(id)
        greeting.delete()
        return None, 204

    @greet_ns.expect(greet_model)
    @greet_ns.marshal_with(greet_model)
    def put(self, id):
        """Update a greeting by ID"""
        greeting = Greet.query.get_or_404(id)
        data = greet_ns.payload
        greeting.msg = data["msg"]
        greeting.save()
        return greeting
