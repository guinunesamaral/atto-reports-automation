from Campanha.Campanha import Campanha
from selenium.webdriver.common.by import By
from Relatorio.TiposDeRelatoriosEnum import TiposDeRelatoriosEnum
from Campanha.TiposDeCampanhasEnum import TiposDeCampanhasEnum


class CampanhaReceptiva(Campanha):
    def __init__(self, browser):
        self.browser = browser

    def selecionar_relatorio(self, tipo_de_relatorio: TiposDeRelatoriosEnum):
        self.browser.find_element(By.ID, "mnuCI").click()

        relatorio_id = ""
        match tipo_de_relatorio:
            case TiposDeRelatoriosEnum.PESQUISA_SATISFACAO:
                relatorio_id = "myGrid-cell-0-3-box"

        self.switch_to_iframe_report_content(
            TiposDeCampanhasEnum.RECEPTIVA, relatorio_id)
