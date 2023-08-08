import logging
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from Relatorio.Relatorio import Relatorio
from Campanha.RecursosHumanos import RecursosHumanos
from Relatorio.TiposDeRelatoriosEnum import TiposDeRelatoriosEnum


class RelatorioAgentActionsHistorico(Relatorio, RecursosHumanos):
    def __init__(self, browser: webdriver.Chrome, logger: logging):
        self.browser = browser
        self.logger = logger

    def executar(self):
        try:
            self.logger.info(
                f"{datetime.now()}, Started RelatorioAgentActionsHistorico")
            self.selecionar_relatorio(
                TiposDeRelatoriosEnum.AGENT_ACTIONS_HISTORICO)
            self.preencher_formulario()
            self.baixar()
            self.logger.info(
                f"{datetime.now()}, Finished RelatorioAgentActionsHistorico")
        except Exception as e:
            self.logger.error(f"{datetime.now()}, {e=}")

    def preencher_formulario(self):
        self.switch_to_iframe_data()

        yesterday = datetime.today() - timedelta(days=1)
        yesterday_formatted = yesterday.strftime('%d%m%Y')

        data = self.browser.find_element(By.ID, "Edit1")
        data.send_keys(yesterday_formatted)

        hora_inicio = self.browser.find_element(By.ID, "Edit2")
        hora_inicio.send_keys("000000")

        hora_fim = self.browser.find_element(By.ID, "Edit3")
        hora_fim.send_keys("235959")

        ok_btn = self.browser.find_element(By.ID, "A1")
        ok_btn.click()

        self.switch_to_window_relatorios()

    def baixar(self):
        self.switch_to_iframe_report()
        self.browser.find_element(By.ID, "btnSave").click()
        self.browser.find_element(By.ID, "divSaveCSV").click()
