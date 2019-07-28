"""Config file for flask application"""
import joblib

class Development(object):
    NAME="Development"

    DEBUG=True
    PORT=None

    REDIS_HOST="localhost"
    REDIS_PORT=6379
    REDIS_PASSWORD="******"


class Production(object):
    NAME="Production"

    DEBUG=False
    PORT=None

    REDIS_HOST="localhost"
    REDIS_PORT=6379
    REDIS_PASSWORD="******"
