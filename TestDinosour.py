from numpy import *
import pyautogui
from PIL import ImageGrab, ImageOps
import time

class Coordinates:
    res_btn = (1024, 384)
    dino_head = (836, 447)


def restart():
    pyautogui.click(Coordinates.res_btn)
    print('Restarted')
    # ImageGrab.grab()


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.18)
    print('Jumped')
    pyautogui.keyUp('space')
    # x = 200 for tree
    # y = 402
    # 893-833

def imagegrab():
    box = (900,445,950,480)
    # box = (Coordinates.dino_head[0]+60, Coordinates.dino_head[1], Coordinates.dino_head[0]+120, Coordinates.dino_head[1]+40)
    img = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(img)
    a = array(grayimage.getcolors())
    print(a.sum())
#     1477 no tree pure white
    return a.sum()

# while True:
#      imagegrab()


def main():
    restart()
    while True:
        if(imagegrab()!=1997):
            pressSpace()
            # time.sleep(0.1)


main()
