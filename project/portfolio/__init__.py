import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create the app
    app = Flask(__name__, instance_relative_config=True)

    # configure the database path here
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite')
    )

    if test_config is None:
        # load the actual config file
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config file
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    ''' ROUTES '''

    from .routes import auth
    app.register_blueprint(auth.bp)

    from .routes import admin
    app.register_blueprint(admin.bp)

    from .routes import stocks
    app.register_blueprint(stocks.bp)

    @app.route('/')
    def index():
        return render_template('index.html', featured=['MSFT', 'AAPL'], portfolio=['WPG', 'AAPL'])

    return app
