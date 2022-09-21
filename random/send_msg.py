import pyautogui as pg
import time


time.sleep(10)

for i in range(0,100):
    pg.write('Message')
    time.sleep(0.25)
    pg.press('Enter')
    time.sleep(0.25)