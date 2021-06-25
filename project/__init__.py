import os

from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app(script_info=None):
    '''
    Inicia APP Flask para MS
    '''

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object("project.config.DevelopmentConfig")

    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # register api
    from project.api import api
    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
