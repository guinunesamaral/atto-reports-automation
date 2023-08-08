from selenium import webdriver
from selenium.webdriver import ChromeOptions
from FileManager.FileManager import FileManager
import chromedriver_autoinstaller


class Browser:
    def __init__(self):
        pass

    # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path
    def install_chromedriver(self):
        chromedriver_autoinstaller.install()

    def get_chrome(self):
        self.install_chromedriver()

        file_manager = FileManager()
        prefs = {
            'download.default_directory': file_manager.concatenar_root_com_path('downloads')}

        options = ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("--headless=new")

        return webdriver.Chrome(options=options)
