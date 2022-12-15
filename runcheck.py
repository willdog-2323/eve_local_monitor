import psutil
from test import imToString
from update import masterList
import PySimpleGUI as sg
right_x = 0
right_y = 0
left_x = 0
left_y = 0
close = 0

def runApp(right_x, right_y, left_x, left_y):
    while "exefile.exe" in (i.name() for i in psutil.process_iter()):
        imToString(right_x, right_y, left_x, left_y)
        masterList()
        if close == 1:
            break

