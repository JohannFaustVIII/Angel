import pyautogui as pg
import time
import sys

if __name__ == "__main__":
    
    print(len(sys.argv))
    message = sys.argv[1]
    repeat = int(sys.argv[2])    

    time.sleep(10)

    for i in range(0,repeat):
        pg.write(message)
        time.sleep(0.25)
        pg.press('Enter')
        time.sleep(0.25)