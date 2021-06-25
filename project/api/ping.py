from flask_restplus import Namespace, Resource

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "ok"}, 200, {'Server': '-'}


ping_namespace.add_resource(Ping, "")
