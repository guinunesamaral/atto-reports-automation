from selenium import webdriver
from selenium.webdriver.common.by import By
from Campanha.Campanha import Campanha


class CampanhaAtiva(Campanha):
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def selecionar_relatorio(self, relatorio_nome):
        self.browser.find_element(By.ID, "mnuCO").click()

        relatorio_id = ""
        match relatorio_nome:
            case "CallHistoryHistorico":
                relatorio_id = "myGrid-cell-0-1-box"
            case "HistoricoCallback":
                relatorio_id = "myGrid-cell-0-2-box"
            case "DiallerCallsHistorico":
                relatorio_id = "myGrid-cell-0-4-box"

        self.switch_to_iframe_report_content(
            "CampanhaAtiva", relatorio_id)
