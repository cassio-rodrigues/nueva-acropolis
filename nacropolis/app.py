from flask import Flask

from nacropolis.ext import configuration


def minimal_app():
    """versao minima da aplicacao, caso que queria testar coisas antes de importar extensoes"""
    app = Flask(__name__)
    configuration.init_app(app)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app

