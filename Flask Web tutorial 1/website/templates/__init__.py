from flask import flask


def create_app():
    app = Flask(_name_)
    app.config['Secret_KEY'] = 'ujmnjkl'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url)

    return app

