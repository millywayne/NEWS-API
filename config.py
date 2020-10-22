 import os

class Config:
    '''
    General configuration parent class
    '''
   
    MOVIE_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=487c722040f046eaa31635a68e73583c'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 