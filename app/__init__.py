from distutils.debug import DEBUG
import os
from flask import Flask
import RPi.GPIO as GPIO
import time


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path=''
    )

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess',
        # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(app.instance_path, 'app.db'),
        # SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True
    )

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # from flask_sslify import SSLify
    # if 'DYNO' in os.environ:  # only trigger SSLify if the app is running on Heroku
    #     sslify = SSLify(app)

    # from app.model import db, migrate
    # db.init_app(app)
    # migrate.init_app(app, db)

    # left - 7, 8, 11
    # right - 10, 12, 13

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(11, 100)
    GPIO.output(13, 100)

    from app.controller import (
        main, pwa
    )
    app.register_blueprint(main.bp)
    app.register_blueprint(pwa.bp)

    return app
