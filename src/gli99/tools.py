from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import json
import os
import re

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

    def __init__(self,browser="edge"):
        self.browser=browser
        self.sources = []
        self.options = None
        
	abspath = os.path.abspath(__file__)
        root = os.path.dirname(abspath)
        options_path = os.path.normpath(root + "/browser_options.json")

        options_json = json.load(open('browser_options.json','r'))
        
        print(f"attempting to create {browser} driver ",end="... ")
        
        def set_browser_options():
            if self.browser.lower() in options_json:
                [self.options.add_argument(arg) for arg in options_json[self.browser.lower()]["arguments"]]
                [self.options.set_preference(pref,value) for pref,value in options_json[self.browser.lower()]["preferences"].items()]
            
        match self.browser.lower():
            case "firefox":
                from selenium.webdriver.firefox.service import Service as FirefoxService
                from webdriver_manager.firefox import GeckoDriverManager
                from selenium.webdriver.firefox.options import Options as FirefoxOptions
                self.options = FirefoxOptions()
                set_browser_options()
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=self.options)
            case "chrome":
                from selenium.webdriver.chrome.service import Service as ChromeService
                from webdriver_manager.chrome import ChromeDriverManager
                from selenium.webdriver.chrome.options import Options as ChromeOptions
                self.options = ChromeOptions()
                set_browser_options()
                self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=self.options)
            case "edge":
                from selenium.webdriver.edge.service import Service as EdgeService
                from webdriver_manager.microsoft import EdgeChromiumDriverManager
                from selenium.webdriver.edge.options import Options as EdgeOptions
                self.options = EdgeOptions()
                set_browser_options()
                self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=self.options)
            case other:
                raise Exception("Browser not supported")
        print("success!")

    def quit(self):
        if not (self.driver.session_id is None):
            self.driver.quit()
            self.driver.session_id = None
            print("driver quit!")
            
    def QuitOnException(func):
        def inner(self,*args,**kwargs):
            try:
                func(self,*args,**kwargs)
            except Exception as e:
                self.quit()
                raise e.with_traceback
        return inner

    @QuitOnException
    def download(self,directory="."):
        directory = directory.replace("\\","/")
        directory = directory if directory[-1] == "/" else directory+"/"
        print("downloading gifs...")
        for source_url in self.sources:
            response = requests.get(source_url)
            file_path = directory+source_url[source_url.rfind('/')+1:]
            print(f"downloading {file_path} ",end="... ")
            open(file_path, "wb").write(response.content)
            print("success!")
        print("all gifs downloaded")

    @QuitOnException
    def load(self,query,amount=10,quit_after_load=True,overwrite_sources=True):
        print(f"retrieving \"{query}\" gifs ",end="... ")
        self.driver.get(f"https://www.gifcities.org/?q={query}")
        WebDriverWait(self.driver,timeout=30,poll_frequency=1).until(did_query_load)
        gifs = self.driver.find_elements(By.CSS_SELECTOR,gif_query_selector)[len(ignored_img_sources):]
        new_sources = list([re.sub("(?<=[0-9])[/](?=http)","if_/",gif.get_attribute("src")) for gif in gifs])[:amount]
        self.sources = new_sources if overwrite_sources else self.sources + new_sources
        if quit_after_load:
            self.driver.quit()
        print("success!")