import time
import msvcrt

from web_conatiner import WebContainer
from web import WebMode

container = WebContainer()

container.addWeb(WebMode.SIM, 1)

def onKeyDown(key):
    if key == 'q':
        print("Exiting...")

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode()
        if key == 'q':
            print("Exiting...")
            break
    time.sleep(0.5)

container.closeAll()