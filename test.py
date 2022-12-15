import pytesseract
from PIL import ImageGrab
from PIL import Image
import cv2
import numpy as nm
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
right_x = 0
right_y = 0
left_x = 0
left_y = 0
def imToString(right_x, right_y, left_x, left_y):
    # Path of tesseract executable
    with open("parsed.txt", "r") as parsed, open("archive.txt", "w") as archive:
        for line in parsed:
            archive.write(line)

        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
    cap = ImageGrab.grab(bbox=(right_x, right_y, left_x, left_y))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
    file = open("screen.txt", "w")
    file.write(tesstr)
    file.close()
    #Image._show(cap)
    with open("screen.txt", "r") as screen, open("parsed.txt", "w") as parsed:
        for line in screen:
            if line.strip():
                parsed.write(line)
    parsed.close()
    screen.close()

    with open("archive.txt", "r") as archive, open("parsed.txt", "r") as parsed:
        inLocal = len(parsed.readlines())
        wereInLocal = len(archive.readlines())
        print(inLocal - wereInLocal)
        delta = inLocal - wereInLocal
        if delta > 0:
            playsound("C:\\Users\\willd\\Downloads\\beep-warning-6387.mp3")


    archive.close()
    parsed.close()



# Calling the function
#imToString()
