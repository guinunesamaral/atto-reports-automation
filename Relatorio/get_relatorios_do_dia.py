import logging
from datetime import datetime
from selenium import webdriver
from Relatorio.RelatorioCallHistoryHistorico import RelatorioCallHistoryHistorico
from Relatorio.RelatorioHistoricoCallback import RelatorioHistoricoCallback
from Relatorio.RelatorioDiallerCallsHistorico import RelatorioDiallerCallsHistorico
from Relatorio.RelatorioPesquisaSatisfacao import RelatorioPesquisaSatisfacao
from Relatorio.RelatorioAgentActionsHistorico import RelatorioAgentActionsHistorico


def get_relatorios_do_dia(browser: webdriver.Chrome, logger: logging):
    relatorios = []

    dia = datetime.today().strftime("%A")
    if dia == "Monday":
        relatorios = [
            RelatorioCallHistoryHistorico(browser, logger)
        ]
    else:
        relatorios = [
            RelatorioCallHistoryHistorico(browser, logger),
            RelatorioHistoricoCallback(browser, logger),
            RelatorioDiallerCallsHistorico(browser, logger),
            RelatorioPesquisaSatisfacao(browser, logger),
            RelatorioAgentActionsHistorico(browser, logger)
        ]
    return relatorios
