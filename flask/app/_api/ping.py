from flask_restx import Namespace, Resource, fields

ping_ns = Namespace("ping", description="Ping! Pong!")

ping_model = ping_ns.model(
    "Ping",
    {
        "status": fields.String(
            required=True, description="The status of the ping request"
        ),
        "message": fields.String(
            required=True, description="The message of the ping request"
        ),
    },
)


@ping_ns.route("/")
class Ping(Resource):
    @ping_ns.doc("ping")
    @ping_ns.marshal_with(ping_model)
    def get(self):
        """Ping the server"""
        return {"status": "success", "message": "pong"}


@ping_ns.route("/<string:msg>")
class PingMsg(Resource):
    @ping_ns.doc("ping_msg")
    @ping_ns.marshal_with(ping_model)
    def get(self, msg):
        """Ping the server"""
        return {"status": "success", "message": msg}
