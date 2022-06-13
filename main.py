from selenium import webdriver
from Atto.Atto import Atto
from Relatorio.RelatorioCallHistoryHistorico import RelatorioCallHistoryHistorico
from Relatorio.RelatorioHistoricoCallback import RelatorioHistoricoCallback
from Relatorio.RelatorioDiallerCallsHistorico import RelatorioDiallerCallsHistorico
from Relatorio.RelatorioPesquisaSatisfacao import RelatorioPesquisaSatisfacao
from Relatorio.RelatorioAgentActions import RelatorioAgentActions
from FileManager.FileManager import FileManager

file_manager = FileManager()
file_manager.clear_directory("downloads")

options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': file_manager.join_root_with_path('downloads')}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=options)

atto = Atto(browser)
atto.login()
atto.open_window_relatorios()
atto.switch_to_window_relatorios()

relatorio_call_history_historico = RelatorioCallHistoryHistorico(
    browser, file_manager)
relatorio_historico_callback = RelatorioHistoricoCallback(
    browser, file_manager)
relatorio_dialler_calls_historico = RelatorioDiallerCallsHistorico(
    browser, file_manager)
relatorio_pesquisa_satisfacao = RelatorioPesquisaSatisfacao(
    browser, file_manager)
relatorio_agent_actions = RelatorioAgentActions(browser, file_manager)

relatorios = [relatorio_call_history_historico,
              relatorio_historico_callback,
              relatorio_dialler_calls_historico,
              relatorio_pesquisa_satisfacao,
              relatorio_agent_actions]

for r in relatorios:
    r.execute()
    atto.refresh_page()

atto.quit()
