from bot.get_from_bank import click_grapes_bank, click_jug_bank
from bot.inventory import click_grapes_inventory, click_jug_inventory
from bot.deposit_to_bank import click_bank, deposit_wine
import pyautogui
import time
from random import uniform


def main():
    while True:
        time.sleep(round(uniform(0.08, 0.12), 2))
        click_grapes_bank()
        click_jug_bank()
        pyautogui.press("esc")
        click_grapes_inventory()
        click_jug_inventory()
        pyautogui.press("space")
        time.sleep(round(uniform(17, 18), 2))
        click_bank()
        deposit_wine()
        time.sleep(round(uniform(0.08, 0.12), 2))


if __name__ == "__main__":
    time.sleep(5)
    main()
