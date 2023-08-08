from time import sleep
from selenium.webdriver.common.by import By
from AttoSite.AttoSite import AttoSite
from Campanha.TiposDeCampanhasEnum import TiposDeCampanhasEnum


class Campanha(AttoSite):
    def __init__(self, browser):
        pass

    def selecionar_relatorio(self, relatorio_nome):
        pass

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

    def switch_to_iframe_report_content(self, tipo_de_campanha: TiposDeCampanhasEnum, relatorio_id):
        sleep(1)
        campanha_id = ""
        match tipo_de_campanha:
            case TiposDeCampanhasEnum.ATIVA:
                campanha_id = "frmCampOutbound_content"
            case TiposDeCampanhasEnum.RECEPTIVA:
                campanha_id = "frmCampInbound_content"
            case TiposDeCampanhasEnum.RECURSOS_HUMANOS:
                campanha_id = "frmHumanResources_content"

        iframe_relatorios = self.browser.find_element(By.ID, campanha_id)
        self.browser.switch_to.frame(iframe_relatorios)

        self.browser.find_element(By.ID, relatorio_id).click()
        self.browser.find_element(By.ID, "btnLupa").click()

        self.switch_to_window_relatorios()
