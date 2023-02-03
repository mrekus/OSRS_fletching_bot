import win32api
import win32con
import time
from random import randint


def click_grapes_bank(x=randint(966, 969), y=randint(118, 122)):
    win32api.SetCursorPos((x, y))
    time.sleep(0.47)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.09)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.12)


def click_jug_bank(x=randint(1014, 1018), y=randint(118, 122)):
    win32api.SetCursorPos((x, y))
    time.sleep(0.53)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)
