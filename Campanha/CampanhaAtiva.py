from Campanha.Campanha import Campanha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CampanhaAtiva(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def select_relatorio(self, nome_relatorio):
        self.browser.find_element(By.ID, "mnuCO").click()
        match nome_relatorio:
            case "CallHistoryHistorico":
                self.id_relatorio = "myGrid-cell-0-1-box"
            case "HistoricoCallback":
                self.id_relatorio = "myGrid-cell-0-2-box"
            case "DiallerCallsHistorico":
                self.id_relatorio = "myGrid-cell-0-4-box"

        self.switch_to_iframe_report_content(
            "CampanhaAtiva", self.id_relatorio)
