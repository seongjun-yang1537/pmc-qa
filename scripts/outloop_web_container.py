from typing import List

from outloop_web import OutloopWeb
from parser import to_json

class OutloopWebContainer:
    def __init__(self, count):
        self.count = count
        self.webs = []
        for i in range(count):
            print('Initialize Web ' + str(i+1))
            self.webs.append(OutloopWeb())
        print('Initialize Web Complete')
            
        self.logger = OutloopWebContainerLogger(self.webs)
        
    def close(self):
        for web in self.webs:
            web.close()
    
    def update(self, seeds):
        for web in self.webs:
            web.update()
            self.logger.update()
            if web.is_finish():
                if web.is_found():
                    seeds.append(web.seed)
                    print(len(seeds), 'find seed', web.seed)
                    print('now', seeds)
                web.reload()
                    
from datetime import datetime
                    
class OutloopWebContainerLogger:
    def __init__(self, webs):
        self.webs: List[OutloopWeb] = webs
        self.date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        
        self.logs = []
        
    def get_file_name(self):
        return "logs/" + self.date + "-outloop-web.json"
    
    def write(self):
        with open(self.get_file_name(), 'w') as log_file:
            log_file.write(to_json(self.logs))
    
    def record(self):
        for web in self.webs:
            if web.is_finish():
                self.logs.append(web.get_log())
                
    def update(self):
        self.record()
        self.write()