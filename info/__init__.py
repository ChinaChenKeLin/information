from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from config import config_dict


db = SQLAlchemy()
redis_obj = None  # type:StrictRedis


def create_app(config_name):
    config_class = config_dict[config_name]

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    global redis_obj
    redis_obj = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, decode_responses=True)

    Session(app)

    return app