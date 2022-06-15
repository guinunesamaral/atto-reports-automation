from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os


class Atto:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def login(self):
        self.browser.get(
            "https://cloud.attodigital.com/AttoSolution/WebLogin/frmLoginAgentClient.aspx")
        print(os.environ.get("NAKTON_ATTO_LOGIN"))
        print(os.environ.get("NAKTON_ATTO_PASSWORD"))

        login_input = self.browser.find_element(By.ID, "edtLogin")
        login_input.clear()
        login_input.send_keys(os.environ.get("NAKTON_ATTO_LOGIN"))

        pwd_input = self.browser.find_element(By.ID, "edtPws")
        pwd_input.clear()
        pwd_input.send_keys(os.environ.get("NAKTON_ATTO_PASSWORD"))

        self.browser.find_element(By.ID, "login-button").click()

    def open_window_relatorios(self):
        delay = 60

        WebDriverWait(self.browser, delay).until(
            EC.presence_of_element_located((By.ID, "btnReporting")))

        self.browser.find_element(By.ID, "btnReporting").click()

    def switch_to_window_relatorios(self):
        sleep(1)
        relatorios = self.browser.window_handles[1]
        self.browser.switch_to.window(relatorios)

    def switch_to_main_window(self):
        sleep(1)
        self.browser.switch_to.default_content()

    def refresh_page(self):
        sleep(1)
        self.browser.refresh()

    def quit(self):
        sleep(1)
        self.browser.quit()

    def switch_to_iframe_report_content(self, nome_campanha, campaign_id):
        sleep(1)
        match nome_campanha:
            case "CampanhaAtiva":
                self.id_campanha = "frmCampOutbound_content"
            case "CampanhaReceptiva":
                self.id_campanha = "frmCampInbound_content"
            case "RecursosHumanos":
                self.id_campanha = "frmHumanResources_content"

        iframe_relatorios = self.browser.find_element(
            By.ID, self.id_campanha)
        self.browser.switch_to.frame(iframe_relatorios)
        self.browser.find_element(By.ID, campaign_id).click()
        self.browser.find_element(By.ID, "btnLupa").click()

        self.switch_to_window_relatorios()

    def switch_to_iframe_data(self):
        sleep(1)
        iframe_data = self.browser.find_element(
            By.ID, "frmReportFilterShow_content")
        self.browser.switch_to.frame(iframe_data)

    def switch_to_iframe_report(self):
        sleep(1)
        iframe_report = self.browser.find_element(
            By.ID, "frmReportPreview_content")
        self.browser.switch_to.frame(iframe_report)
