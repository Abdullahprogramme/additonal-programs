import pyautogui as pag
import time
import random as r

for i in range(10):
    x = r.randint(600, 900)
    y = r.randint(400, 600)
    pag.moveTo(x, y, 0.5)
    time.sleep(2.5)
