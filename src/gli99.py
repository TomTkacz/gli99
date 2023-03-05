from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import re
import requests

gif_query_selector = "div a img"
ignored_img_sources = [
    "https://web.archive.org/web/20090804113154/http://geocities.com/SunsetStrip/Lounge/7650/dollarspindownd.gif",
    "https://gifcities.org/assets/internetarchive.svg",
]

def set_profile_preferences(profile):
    profile.add_argument("-headless")
    profile.set_preference("network.http.pipelining", True)
    profile.set_preference("network.http.proxy.pipelining", True)
    profile.set_preference("network.http.pipelining.maxrequests", 8)
    profile.set_preference("content.notify.interval", 500000)
    profile.set_preference("content.notify.ontimer", True)
    profile.set_preference("content.switch.threshold", 250000)
    profile.set_preference("browser.cache.memory.capacity", 65536) # Increase the cache capacity.
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("reader.parse-on-load.enabled", False) # Disable reader, we won't need that.
    profile.set_preference("browser.pocket.enabled", False) # Duck pocket too!
    profile.set_preference("loop.enabled", False)
    profile.set_preference("browser.chrome.toolbar_style", 1) # Text on Toolbar instead of icons
    profile.set_preference("browser.display.show_image_placeholders", False) # Don't show thumbnails on not loaded images.
    profile.set_preference("browser.display.use_document_colors", False) # Don't show document colors.
    profile.set_preference("browser.display.use_document_fonts", 0) # Don't load document fonts.
    profile.set_preference("browser.display.use_system_colors", True) # Use system colors.
    profile.set_preference("browser.formfill.enable", False) # Autofill on forms disabled.
    profile.set_preference("browser.helperApps.deleteTempFileOnExit", True) # Delete temprorary files.
    profile.set_preference("browser.shell.checkDefaultBrowser", False)
    profile.set_preference("browser.startup.homepage", "about:blank")
    profile.set_preference("browser.startup.page", 0) # blank
    profile.set_preference("browser.tabs.forceHide", True) # Disable tabs, We won't need that.
    profile.set_preference("browser.urlbar.autoFill", False) # Disable autofill on URL bar.
    profile.set_preference("browser.urlbar.autocomplete.enabled", False) # Disable autocomplete on URL bar.
    profile.set_preference("browser.urlbar.showPopup", False) # Disable list of URLs when typing on URL bar.
    profile.set_preference("browser.urlbar.showSearch", False) # Disable search bar.
    profile.set_preference("extensions.checkCompatibility", False) # Addon update disabled
    profile.set_preference("extensions.checkUpdateSecurity", False)
    profile.set_preference("extensions.update.autoUpdateEnabled", False)
    profile.set_preference("extensions.update.enabled", False)
    profile.set_preference("general.startup.browser", False)
    profile.set_preference("plugin.default_plugin_disabled", False)
    profile.set_preference("permissions.default.image", 2) # Image load disabled again


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
        match self.browser.lower():
            case "firefox":
                self.options = Options()
                set_profile_preferences(self.options)
                self.driver = webdriver.Firefox(options=self.options)
            case other:
                print("browser not supported")

    def quit(self):
        self.driver.quit()

    def download(self,directory):
        print("downloading...")
        for source_url in self.sources:
            response = requests.get(source_url)
            file_path = directory+source_url[source_url.rfind('/')+1:]
            print(f"downloading {file_path} ",end="... ")
            open(file_path, "wb").write(response.content)
            print("success!")
        print("all gifs downloaded")

    def load(self,query,amount=10):
        self.driver.get(f"https://www.gifcities.org/?q={query}")
        WebDriverWait(self.driver,timeout=30,poll_frequency=1).until(did_query_load)
        gifs = self.driver.find_elements(By.CSS_SELECTOR,gif_query_selector)[len(ignored_img_sources):]
        self.sources = list([re.sub("(?<=[0-9])[/](?=http)","if_/",gif.get_attribute("src")) for gif in gifs])[:amount]
        self.quit()