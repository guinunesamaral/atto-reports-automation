from Campanha.Campanha import Campanha
from selenium.webdriver.common.by import By


class RecursosHumanos(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def selecionar_relatorio(self, relatorio_nome):
        self.browser.find_element(By.ID, "mnuRH").click()
        match relatorio_nome:
            case "AgentActionsHistorico":
                self.relatorio_id = "myGrid-cell-0-1-box"
        self.switch_to_iframe_report_content(
            "RecursosHumanos", self.relatorio_id)
