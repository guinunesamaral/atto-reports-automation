from Campanha.Campanha import Campanha
from selenium.webdriver.common.by import By


class CampanhaReceptiva(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def select_relatorio(self, nome_relatorio):
        self.browser.find_element(By.ID, "mnuCI").click()
        match nome_relatorio:
            case "PesquisaSatisfacao":
                self.id_relatorio = "myGrid-cell-0-3-box"
        self.switch_to_iframe_report_content(
            "CampanhaReceptiva", self.id_relatorio)
