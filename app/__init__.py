from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask import main as main_blueprint


bootstrap = Bootstrap()

def create_app(config_name, config_options):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


# Initializing application
app = Flask(__name__, instance_relative_config = True)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap.init_app(app)

 # Registering the blueprint
app.register_blueprint(main_blueprint,)





from app import views
from app import error

