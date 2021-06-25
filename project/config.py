import os


class BaseConfig:
    TESTING = False


class DevelopmentConfig(BaseConfig):
    TESTING = False


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    TESTING = False
