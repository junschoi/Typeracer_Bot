# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import sys

class TypeRacer:
    def __init__(self):
        print('TypeRacer Bot 1.0 by junschoi')
        print('List of commands: ')
        print('=========================================')
        print('public             | Play a public game')
        print('practice           | Play a practice game')
        print('private            | Join a private game')
        print('exit')
        print('\n')
        options = Options()
        # Add below line to the code if you keep receiving "WSALookupServiceBegin failed with: 0" error message
        # options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # Set path as your ChromeDriver path below
        path = r'driver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path, options = options)
        self.menu()

    def menu(self):
        while True:
            cmd = input('Enter a command: \n>> ')
            cmd = cmd.lower()
            if cmd in ('public', 'practice', 'private', 'exit'):
                if cmd == 'public':
                    self.play_public()
                elif cmd == 'practice':
                    self.play_practice()
                elif cmd == 'private':
                    self.play_private()
                elif cmd == 'exit':
                    try: 
                        self.driver.quit()
                        sys.exit()
                    except:
                        pass
                    finally:
                        sys.exit()
            else:
                print('Invalid command')        
 
    def play_public(self):
        self.driver.get(r'https://play.typeracer.com')
        time.sleep(1)
        race = self.driver.find_element_by_partial_link_text('Enter a typing race')
        race.click()
        time.sleep(1)
        self.play()

    def play_practice(self):
        self.driver.get(r'https://play.typeracer.com')
        time.sleep(1)
        race = self.driver.find_element_by_partial_link_text('Practice')
        race.click()
        time.sleep(1)
        self.play()

    def play_private(self):
        private_url = input('Enter private match url: ')
        try:
            self.driver.get(private_url)
            time.sleep(1)
            race = self.driver.find_element_by_partial_link_text('join race')
            race.click()
            time.sleep(1)
            self.play()
        except:
            print('Invalid url')

    def play(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME,'txtInput')))
            input_panel = self.driver.find_element_by_class_name('inputPanel')
            text = input_panel.text
            text = text[:text.find('\n')]
            txtinput = self.driver.find_element_by_class_name('txtInput')
            for char in text:
                txtinput.send_keys(char)
                time.sleep(0.01)
        except:
            print('Timed out')

if __name__ == "__main__":
    TypeRacer()
