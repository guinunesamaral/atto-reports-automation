import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from FileManager.FileManager import FileManager


class Browser:
    def __init__(self):
        pass

    def get_chrome(self):
        file_manager = FileManager()
        prefs = {
            'download.default_directory': file_manager.concatenar_root_com_path('downloads')}

        options = ChromeOptions()
        options.binary_location = os.environ.get("CHROME_FOR_TESTING_PATH")
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("--headless=new")

        return webdriver.Chrome(options=options)
