from redis import StrictRedis

class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SECRET_KEY = 'DAJWOIFOSNDFJSDNFALKALKSNFA-FA--FAFMKLAMNFKA-SF-ASFMLKASFNLAKS'

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=1)
    SESSION_USE_SIGNER = True   # 是否加密
    SESSION_PERMANENT = False   # 过期时间是否永久
    PERMANENT_SESSION_LIFETIME = 36000  # 过期时长  秒


class DevelopmentConfig(Config):
    DEBUG = True


class ProducetionConfig(Config):
    DEBUG = False


config_dict = {
    'developmentconfig':DevelopmentConfig,
    'producetion':ProducetionConfig
}