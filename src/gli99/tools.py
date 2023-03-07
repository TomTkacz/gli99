from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json
import os
import re
import requests

gif_query_selector = "div a img"
ignored_img_sources = [
    "https://web.archive.org/web/20090804113154/http://geocities.com/SunsetStrip/Lounge/7650/dollarspindownd.gif",
    "https://gifcities.org/assets/internetarchive.svg",
]


def did_query_load(driver):
    try:
        elements = driver.find_elements(By.CSS_SELECTOR,gif_query_selector)
        for element in elements:
            if element.get_attribute("src") in ignored_img_sources:
                continue
            return True
        return False
    except:
        return False

class GifScraper():

    def __init__(self,browser="firefox"):
        self.browser=browser
        self.sources = []
        self.options = Options()
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        options_json = json.load(open('browser_options.json','r'))
        
        if self.browser.lower() in options_json:
            [self.options.add_argument(arg) for arg in options_json[self.browser.lower()]["arguments"]]
            [self.options.set_preference(pref[0],pref[1]) for pref in options_json[self.browser.lower()]["preferences"]]
            
        print(f"attempting to create {browser} driver ",end="... ")
        match self.browser.lower():
            case "firefox":
                self.driver = webdriver.Firefox(options=self.options)
            case "chrome":
                self.driver = webdriver.Chrome(options=self.options)
            case other:
                print("browser not supported")
                return
        print("success!")

    def quit(self):
        self.driver.quit()

    def download(self,directory):
        directory = directory.replace("\\","/")
        directory = directory if directory[directory.rfind("/"):][-1] == "/" else directory+"/"
        print("downloading gifs...")
        for source_url in self.sources:
            response = requests.get(source_url)
            file_path = directory+source_url[source_url.rfind('/')+1:]
            print(f"downloading {file_path} ",end="... ")
            open(file_path, "wb").write(response.content)
            print("success!")
        print("all gifs downloaded")

    def load(self,query,amount=10):
        print(f"retrieving {query} gifs ",end="... ")
        self.driver.get(f"https://www.gifcities.org/?q={query}")
        WebDriverWait(self.driver,timeout=30,poll_frequency=1).until(did_query_load)
        gifs = self.driver.find_elements(By.CSS_SELECTOR,gif_query_selector)[len(ignored_img_sources):]
        self.sources = list([re.sub("(?<=[0-9])[/](?=http)","if_/",gif.get_attribute("src")) for gif in gifs])[:amount]
        print("success!")
        self.quit()