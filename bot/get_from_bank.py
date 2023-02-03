import win32api
import win32con
import time
from random import randint, uniform


def click_grapes_bank(x=randint(966, 969), y=randint(118, 122)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))


def click_jug_bank(x=randint(1014, 1018), y=randint(118, 122)):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.40, 0.49), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(round(uniform(0.09, 0.12), 2))
