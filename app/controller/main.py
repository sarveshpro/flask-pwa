from flask import (
    Blueprint, render_template, Response
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html',
                           title='UV Disinfectant Bot')


direction = 'stop'


@bp.route('/forward')
def forward():
    direction = 'forward'
    return Response({
        direction
    }, 200)


@bp.route('/backward')
def backward():
    direction = 'backward'
    return Response(direction, 200)


@bp.route('/left')
def left():
    direction = 'left'
    return Response(direction, 200)


@bp.route('/right')
def right():
    direction = 'right'
    return Response(direction, 200)


@bp.route('/stop')
def stop():
    direction = 'stop'
    return Response(direction, 200)
