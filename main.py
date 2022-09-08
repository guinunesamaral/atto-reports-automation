from datetime import datetime
import logging
from selenium import webdriver
from Atto.Atto import Atto
from Relatorio.RelatorioCallHistoryHistorico import RelatorioCallHistoryHistorico
from Relatorio.RelatorioHistoricoCallback import RelatorioHistoricoCallback
from Relatorio.RelatorioDiallerCallsHistorico import RelatorioDiallerCallsHistorico
from Relatorio.RelatorioPesquisaSatisfacao import RelatorioPesquisaSatisfacao
from Relatorio.RelatorioAgentActionsHistorico import RelatorioAgentActionsHistorico
from FileManager.FileManager import FileManager


def main():
    file_manager = FileManager()
    file_manager.clear_directory("downloads")

    options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': file_manager.join_root_with_path('downloads')}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("headless")
    browser = webdriver.Chrome(options=options)

    atto = Atto(browser)
    logging.basicConfig(
        filename=file_manager.atto_reports_automation_log, level=logging.INFO)
    try:
        logging.info(
            f"{datetime.now()}, Started Login")
        atto.login()
        logging.info(
            f"{datetime.now()}, Finished Login")
        atto.open_window_relatorios()
        atto.switch_to_window_relatorios()
    except Exception as e:
        logging.error(f"{datetime.now()}, {e=}")

    day = datetime.today().strftime("%A")
    relatorios = []

    if day == "Monday":
        relatorios = [
            RelatorioCallHistoryHistorico(browser, file_manager)
        ]
    else:
        relatorios = [
            RelatorioCallHistoryHistorico(browser, file_manager),
            RelatorioHistoricoCallback(browser, file_manager),
            RelatorioDiallerCallsHistorico(browser, file_manager),
            RelatorioPesquisaSatisfacao(browser, file_manager),
            RelatorioAgentActionsHistorico(browser, file_manager)
        ]

    for r in relatorios:
        r.execute()
        atto.refresh_page()

    atto.quit()


if __name__ == "__main__":
    main()
