import win32api
import pyautogui
import time
from random import randint, uniform


def click_bow_inventory(x=randint(1130, 1142), y=randint(347, 362)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))


def click_string_inventory(x=randint(1128, 1146), y=randint(387, 402)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.02, 0.05), 2)))
    time.sleep(round(uniform(0.07, 0.10), 2))
