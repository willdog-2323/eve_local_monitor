import pynput.mouse
from pynput.mouse import Listener

rx = 0
ry = 0

lx = 0
ly = 0

def on_clickr(x, y ,button, pressed):
    print((x, y))
    rx = x
    ry = y
    print((rx, ry))
    listener.stop()

def on_clickl(x, y ,button, pressed):
    print((x, y))
    lx = x
    ly = y
    print((lx, ly))
    listener.stop()


# Collect events until released




