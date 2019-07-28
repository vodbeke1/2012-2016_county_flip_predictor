"""Config file for flask application"""
import joblib

class Development(object):
    NAME="Development"

    DEBUG=True


class Production(object):
    NAME="Production"

    DEBUG=False

