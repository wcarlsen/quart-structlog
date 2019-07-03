class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True


class Staging(Config):
    pass


class Production(Config):
    DEBUG = False


config = {
    "development": Development,
    "staging": Staging,
    "production": Production,
    "default": Development,
}
