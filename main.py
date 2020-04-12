# Open Chrome with https://virtualpiano.net/

import pyautogui
import numpy as np
import time


def move_and_click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.leftClick()


def run_half_notes():
    y = 380


def run_whole_notes():
    c = 0
    n_steps = 10
    delta_steps = 1

    y = 450
    x_start = 197
    x_end = 366
    step_size = (x_end - x_start)/7
    x_start = x_start + delta_steps*step_size
    x_prev = x_start + 2*step_size

    while True:
        i = np.random.randint(n_steps)
        x = x_start + i * step_size
        while x == x_prev:
            i = np.random.randint(n_steps)
            x = x_start + i*step_size
        x_prev = x
        move_and_click(x, y)

        time.sleep(7.5)
        c += 1
        print(c)


run_whole_notes()
