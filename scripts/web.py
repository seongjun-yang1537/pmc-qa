import json
import random

from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# region constant
class WebMode(Enum):
    SIM = ""
    TESTBED = "testbed"
    OUTLOOP = "outloop"
    DICE = "dice"

BASE_URL = 'http://localhost:3000'
# endregion

class Web:
    def __init__(self, mode:WebMode = WebMode.SIM):
        self.mode = mode
        self.driver = self.create_driver()

        self.components = []
        self.onStart()

    def create_driver(self):
        options = Options()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.use_chromium = True
        options.add_experimental_option("detach", True)
        options.set_capability('loggingPrefs', { 'browser':'ALL' })

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.create_url())
        return driver
    
    def create_url(self, options=[]):
        url = f"{BASE_URL}/{self.mode.value}?"
        sz = len(options)
        for i in range(sz):
            if i > 0:
                url += '&'
            [key, value] = options[i]
            url += f"{key}={value}"
        return url
    
    def onStart(self):
        
        pass
    
    def onUpdate(self):
        print('update')

    def onClose(self):
        self.driver.close()
        self.driver.quit()
        pass
