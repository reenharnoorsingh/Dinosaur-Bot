import pyautogui
import time
from PIL import Image, ImageGrab
def hit(key):
    pyautogui.press(key)

def check_day():
    for i in range(250,260):
        for j in range(100,120):
            if data[i,j]>150:
                return "day"
            else:
                return "night"

def collide_1(data):
    for i in range(310,340):
        for j in range(400,450):
            if data[i,j]<100:
                return True
    return False

def collide_2(data):
    for i in range(310,340):
        for j in range(400,450):
            if data[i,j]>100:
                return True
    return False


time.sleep(3)
hit("space")
while True:
    image=ImageGrab.grab().convert("L")
    data=image.load()
    if check_day()=="day":
        if collide_1(data):
            hit("up")
    if check_day()=="night":
        if collide_2(data):
            hit("up")