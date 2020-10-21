class Config:
    '''
    General configuration parent class
    '''
    'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=487c722040f046eaa31635a68e73583c'



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