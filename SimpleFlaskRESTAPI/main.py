#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ---------------------------------------------------------------------------
#  Name: main.py
#  Version: 0.0.1
#  Summary: A simple REST API with Python and Flask
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ---------------------------------------------------------------------------

"""Building a simple REST API with Python and Flask."""

from flask import Flask
from flask_restful import Api, Resource

flask_app = Flask(__name__)

rest_api = Api(flask_app)


class HelloWord(Resource):
    @staticmethod
    def get():
        return {
            'mensagem':
                'Hello World, a simple REST API with Python and Flask.'
        }


rest_api.add_resource(HelloWord, '/helloword')

if __name__ == '__main__':
    flask_app.run(debug=True)
