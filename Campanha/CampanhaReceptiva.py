from Campanha.Campanha import Campanha
from selenium.webdriver.common.by import By


class CampanhaReceptiva(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def selecionar_relatorio(self, relatorio_nome):
        self.browser.find_element(By.ID, "mnuCI").click()
        match relatorio_nome:
            case "PesquisaSatisfacao":
                self.relatorio_id = "myGrid-cell-0-3-box"
        self.switch_to_iframe_report_content(
            "CampanhaReceptiva", self.relatorio_id)
