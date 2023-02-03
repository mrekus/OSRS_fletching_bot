from bot.get_from_bank import click_grapes, click_jug
from utils import pyautogui
import time


def main():
    click_grapes()
    click_jug()
    pyautogui.press("esc")


if __name__ == "__main__":
    time.sleep(5)
    main()
