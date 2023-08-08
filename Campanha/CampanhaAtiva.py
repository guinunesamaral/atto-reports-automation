from selenium import webdriver
from selenium.webdriver.common.by import By
from Campanha.Campanha import Campanha
from Relatorio.TiposDeRelatoriosEnum import TiposDeRelatoriosEnum
from Campanha.TiposDeCampanhasEnum import TiposDeCampanhasEnum


class CampanhaAtiva(Campanha):
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def selecionar_relatorio(self, tipo_de_relatorio: TiposDeRelatoriosEnum):
        self.browser.find_element(By.ID, "mnuCO").click()

        relatorio_id = ""
        match tipo_de_relatorio:
            case TiposDeRelatoriosEnum.CALL_HISTORY_HISTORICO:
                relatorio_id = "myGrid-cell-0-1-box"
            case TiposDeRelatoriosEnum.HISTORICO_CALLBACK:
                relatorio_id = "myGrid-cell-0-2-box"
            case TiposDeRelatoriosEnum.DIALER_CALLS_HISTORICO:
                relatorio_id = "myGrid-cell-0-4-box"

        self.switch_to_iframe_report_content(
            TiposDeCampanhasEnum.ATIVA, relatorio_id)
