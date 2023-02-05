import win32api
import time
import pyautogui
from random import randint, uniform


def click_bow_bank(x=randint(3196, 3212), y=randint(112, 129)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))


def click_string_bank(x=randint(3246, 3260), y=randint(112, 129)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))
