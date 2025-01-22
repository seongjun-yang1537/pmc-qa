import threading
import time
from web import Web, WebMode

TPS = 30

class WebContainer:
    def __init__(self):
        self.webs = []
        self.threads = []
        self.close_events : list[threading.Event] = []

    def onWeb(self, web:Web, close_event:threading.Event):
        interval = 1.0 / TPS
        
        while not close_event.is_set():
            now_time = time.time()
            web.onUpdate()
            
            elapsed = time.time() - now_time
            time.sleep(max(0, interval - elapsed))

        web.onClose()

    def addWeb(self, mode:WebMode, count=1):
        for i in range(count):
            web = Web(mode)
            self.webs.append(web)

            close_event = threading.Event()
            thread = threading.Thread(target=self.onWeb, args=(web, close_event))

            self.threads.append(thread)
            self.close_events.append(close_event)

            thread.start()                 

    def close(idx):
        pass

    def closeAll(self):
        for event in self.close_events:
            event.set()

        self.threads = []
        self.close_events = []        
        pass