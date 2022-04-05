import threading
import time

direction = "stop"


def direction_loop():
    global direction
    while True:
        time.sleep(1)
        if direction == 'forward':
            print('moving forward')
        elif direction == 'left':
            print('turning left')
        elif direction == 'backward':
            print('moving backward')
        elif direction == 'right':
            print('turning right')
        elif direction == 'stop':
            print('stopped')
            continue
        else:
            continue


def set_direction(new_direction):
    global direction
    direction = new_direction


def start_flask_server():
    pass


t1 = threading.Thread(target=direction_loop)
t1.start()
