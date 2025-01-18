
import time
import msvcrt

from outloop_web_container import OutloopWebContainer
    
DRIVER_COUNT = 1
web_container = OutloopWebContainer(DRIVER_COUNT)

def onKeyDown(key):
    if key == 'q':
        print("Exiting...")
        web_container.close()

while True:
    if msvcrt.kbhit():
        onKeyDown(msvcrt.getch().decode())
    
    if web_container.update():
        break
    time.sleep(0.5)
    
web_container.close()