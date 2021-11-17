from importlib import import_module

from dynaconf import FlaskDynaconf


def load_extensions(app):
    for extension in app.config.EXTENSIONS:
        # pega as extensoes do arquivo .toml, usar formato "extension.path:factory_funtion"
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        # chamo a factory passando o app.
        getattr(ext, factory)(app)


def init_app(app, **config):
    # funcao necessaria para evitar erro de import circular
    FlaskDynaconf(app, **config)
