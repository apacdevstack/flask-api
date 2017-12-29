"""REST API resources."""

from flask_restful import Resource


class HelloWorldResource(Resource):
    """Helloworld Resource Sample"""

    def get(self):
        """get maps to GET method"""
        return {"message": "Hello World"}
