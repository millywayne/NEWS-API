from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap


# Initializing application
app = Flask(__name__,instance_relative_config = True)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = ' http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=487c722040f046eaa31635a68e73583c'