from flask import (
    Blueprint, render_template, Response
)
import RPi.GPIO as GPIO

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html',
                           title='Smart WiFi Bot')


direction = 'stop'


@bp.route('/forward')
def forward():
    direction = 'forward'
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    return Response({
        direction
    }, 200)


@bp.route('/backward')
def backward():
    direction = 'backward'
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    return Response(direction, 200)


@bp.route('/left')
def left():
    direction = 'left'
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    return Response(direction, 200)


@bp.route('/right')
def right():
    direction = 'right'
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    return Response(direction, 200)


@bp.route('/stop')
def stop():
    direction = 'stop'
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    return Response(direction, 200)
