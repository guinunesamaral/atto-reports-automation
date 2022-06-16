from selenium import webdriver
from Relatorio.Relatorio import Relatorio
from Campanha.CampanhaReceptiva import CampanhaReceptiva
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from FileManager.FileManager import FileManager


class RelatorioPesquisaSatisfacao(Relatorio, CampanhaReceptiva):
    def __init__(self, browser: webdriver.Chrome, file_manager: FileManager):
        self.browser = browser
        self.file_manager = file_manager

    def execute(self):
        self.select_relatorio("PesquisaSatisfacao")
        self.fill_report_form()
        self.save_report()
        self.rename_report()

    def fill_report_form(self):
        self.switch_to_iframe_data()

        yesterday = datetime.today() - timedelta(days=1)
        yesterday_formatted = yesterday.strftime('%d%m%Y')

        data_inicio = self.browser.find_element(By.ID, "Edit1")
        data_inicio.send_keys(yesterday_formatted)

        data_fim = self.browser.find_element(By.ID, "Edit2")
        data_fim.send_keys(yesterday_formatted)

        hora_inicio = self.browser.find_element(By.ID, "Edit3")
        hora_inicio.send_keys("000000")

        hora_fim = self.browser.find_element(By.ID, "Edit4")
        hora_fim.send_keys("235959")

        ok_btn = self.browser.find_element(By.ID, "A1")
        ok_btn.click()

        self.switch_to_window_relatorios()

    def save_report(self):
        self.switch_to_iframe_report()
        self.browser.find_element(By.ID, "btnSave").click()
        self.browser.find_element(By.ID, "divSaveCSV").click()

    def rename_report(self):
        file = self.file_manager.latest_downloaded_file(4)
        downloads_path = self.file_manager.join_root_with_path("downloads")
        old_file_path = self.file_manager.join_paths(downloads_path, file)
        new_file_path = self.file_manager.join_paths(
            downloads_path, "PesquisaSatisfacao.CSV")
        self.file_manager.rename_file(
            old_file_path, new_file_path)
