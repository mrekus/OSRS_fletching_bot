import win32api
import win32con
import time
from random import randint, uniform


def click_bow_inventory(x=randint(1130, 1142), y=randint(347, 362)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))


def click_string_inventory(x=randint(1128, 1146), y=randint(387, 402)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
