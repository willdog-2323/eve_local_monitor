import PySimpleGUI as sg
from runcheck import runApp

from pynput.mouse import Listener


rx = 1
ry = 1
lx = 1
ly = 1

def on_clickr(x, y ,button, pressed):
    global rx
    global ry
    rx = x
    ry = y
    print((rx, ry))
    listener.stop()

def on_clickl(x, y ,button, pressed):
    global lx
    global ly
    lx = x
    ly = y
    print((lx, ly))
    listener.stop()


layout = [[sg.Text("TEXT HERE")], [sg.Button("Run APP")], [sg.Button("Right Coord")], [sg.Button("Left Coord")], [sg.Button("Stop")]]

window = sg.Window(title="Hello World", layout= layout, margins=(100, 50))
close = 0

while True:
    event, values = window.read()
    if event == "Right Coord":
        with Listener(
                on_click=on_clickl,
        ) as listener:
            listener.join()
    if event == "Left Coord":
        with Listener(
                on_click=on_clickr,
        ) as listener:
            listener.join()
    if event == "Run APP":
        runApp(rx, ry, lx, ly)

    if event == "Stop":
        close = 1


