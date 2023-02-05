import win32api
import time
import pyautogui
from random import randint, uniform


def click_bank(x=randint(3499, 3572), y=randint(293, 333)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))


def deposit_bows(x=randint(3551, 3574), y=randint(324, 342)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))
