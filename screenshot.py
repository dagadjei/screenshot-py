import time
import pyautogui

def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot("img.png")
    img.show()

screenshot()