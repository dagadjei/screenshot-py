import time
import pyautogui


def screenshot():
    name = int(round(time.time()*1000))
    # save file in shots directory
    name = "C:/Users/JUDE ASMAH/Desktop/screenshot-py/shots/{}.png".format(name) 
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()