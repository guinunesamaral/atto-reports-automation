from Campanha.Campanha import Campanha
from selenium.webdriver.common.by import By


class RecursosHumanos(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def select_relatorio(self, nome_relatorio):
        self.browser.find_element(By.ID, "mnuRH").click()
        match nome_relatorio:
            case "AgentActions":
                self.id_relatorio = "myGrid-cell-0-0-box"
        self.switch_to_iframe_report_content(
            "RecursosHumanos", self.id_relatorio)
