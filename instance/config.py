import os 
class Config(object):
    
    DEBUG = False
    SECRET = os.getenv('SECRET') 
    
    DATABASE_URI = os.getenv('DATABASE_URL')
class DevelopmentConfig(Config):
    
    DEBUG = True
class TestingConfig(Config):
   
    TESTING = True
    DATABASE_URI = 'testing URL for the test DB'
    DEBUG = True
class StagingConfig(Config):
   
    DEBUG = True
class ProductionConfig(Config):
    
    DEBUG = False
    TESTING = False
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
