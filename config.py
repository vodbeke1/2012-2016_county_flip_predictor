"""Config file for flask application"""
import joblib

class Development(object):
    NAME="Development"

    DEBUG=True
    PORT=7898

    REDIS_HOST="localhost"
    REDIS_PORT=6379
    REDIS_PASSWORD=1206


class Production(object):
    NAME="Production"

    DEBUG=False
    PORT=7898

    REDIS_HOST="localhost"
    REDIS_PORT=6379
    REDIS_PASSWORD="redis1"
