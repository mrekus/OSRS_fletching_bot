import win32api
import pyautogui
import time
from random import randint, uniform


def click_bow_inventory(x=randint(3690, 3702), y=randint(347, 362)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))


def click_string_inventory(x=randint(3688, 3706), y=randint(387, 402)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.09, 0.12), 2)))
    time.sleep(round(uniform(0.09, 0.12), 2))
