import json
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from parser import filter_logs

class OutloopWeb:
    def __init__(self):
        self.seed = 0
        self.driver = self.initialize_driver()
        self.action = self.initialize_action()
        
        self.logs = []
    
    def seed_url(self) :
        self.seed = random.randrange(1, 100000)
        return 'http://localhost:3000/outloop?outloopseed=' + str(self.seed)
    
    def get_chrome_options(self) :
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
        chrome_options.use_chromium = True
        chrome_options.add_experimental_option("detach", True)
        chrome_options.set_capability('loggingPrefs', { 'browser':'ALL' })
        return chrome_options
    
    def initialize_driver(self):
        options = self.get_chrome_options()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(self.seed_url())
        return driver
        
    def initialize_action(self):
        return ActionChains(self.driver)   
        
    def update(self):
        self.action.send_keys(Keys.ESCAPE).perform()
        self.action.send_keys('4').perform()
        
        self.logs += self.driver.get_log('browser')
        
    def reload(self):
        self.driver.get(self.seed_url())    
        self.logs = []

    def close(self):
        self.driver.close()
        
    def get_log(self):
        log = filter_logs(self.logs)
        if log == -1:
            return False
        
        log = str(log).replace('\\','', 4)
        data = json.loads(log)
            
        [res, entity_alive_count] = [int(data['res']), int(data['entity_alive_count'])]
        
        return {
            "res":res,
            "entity_alive_count": entity_alive_count
        }
        
    def is_finish(self):
        return self.get_log() is not False
    
    def is_found(self):
        log = self.get_log()
        if log is False:
            return False

        return log['res'] == 0 and log['entity_alive_count'] == 1