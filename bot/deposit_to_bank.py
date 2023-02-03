import win32api
import win32con
import time
from random import randint


def click_bank(x=randint(1264, 1269), y=randint(321, 324)):
    win32api.SetCursorPos((x, y))
    time.sleep(0.45)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)


def deposit_wine(x=randint(1320, 1324), y=randint(334, 337)):
    win32api.SetCursorPos((x, y))
    time.sleep(0.7)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.11)
