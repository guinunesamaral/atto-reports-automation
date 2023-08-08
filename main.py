from Browser.Browser import Browser
from FileManager.FileManager import FileManager
from Logger.Logger import Logger
from AttoSite.AttoSite import AttoSite
from Relatorio.get_relatorios_do_dia import get_relatorios_do_dia


def main():
    browser = Browser().get_chrome()
    logger = Logger().get_logger()
    file_manager = FileManager()

    atto = AttoSite(browser, logger)
    atto.login()
    atto.abrir_guia_relatorios()
    atto.switch_to_window_relatorios()
    atto.abrir_antigo_portal()

    relatorios = get_relatorios_do_dia(browser, logger)
    for r in relatorios:
        r.executar()
        atto.recarregar_pagina()

    file_manager.renomear_relatorios()
    atto.sair()


if __name__ == "__main__":
    main()
