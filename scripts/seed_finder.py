
import time
import msvcrt

from outloop_web_container import OutloopWebContainer
    
DRIVER_COUNT = 5
TARGET_COUNT = 5 # 찾으려고 하는 시드의 개수
web_container = OutloopWebContainer(DRIVER_COUNT)

def onKeyDown(key):
    if key == 'q':
        print("Exiting...")
        web_container.close()

seeds = []

while len(seeds) < TARGET_COUNT:
    if msvcrt.kbhit():
        onKeyDown(msvcrt.getch().decode())
    
    web_container.update(seeds)
    time.sleep(0.5)
    
print(seeds)
web_container.close()