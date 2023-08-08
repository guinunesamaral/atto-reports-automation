import os
import logging
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class AttoSite:
    def __init__(self, browser: webdriver.Chrome, logger: logging):
        self.browser = browser
        self.logger = logger

    def login(self):
        try:
            self.logger.info(
                f"{datetime.now()}, Login iniciado")
            self.browser.get(os.environ.get("ATTO_URL"))
            self.switch_to_iframe_login()
            self.preencher_email()
            self.preencher_senha()
            self.browser.find_element(By.ID, "login-button-auth").click()
            self.switch_to_main_window()
            self.logger.info(
                f"{datetime.now()}, Login finalizado")
        except Exception as e:
            self.logger.error(f"{datetime.now()}, {e=}")

    def switch_to_iframe_login(self):
        iframe_login = self.browser.find_element(By.ID, "frameRight")
        self.browser.switch_to.frame(iframe_login)

    def preencher_email(self):
        login_input = self.browser.find_element(By.ID, "edtLogin")
        login_input.clear()
        login_input.send_keys(os.environ.get("ATTO_LOGIN"))

    def preencher_senha(self):
        pwd_input = self.browser.find_element(By.ID, "edtPws")
        pwd_input.clear()
        pwd_input.send_keys(os.environ.get("ATTO_PASSWORD"))

    def abrir_guia_relatorios(self):
        sleep(1)
        self.switch_to_iframe_relatorios()
        self.browser.find_elements(By.CLASS_NAME, "button-name")[3].click()

    def abrir_antigo_portal(self):
        sleep(1)
        self.browser.find_element(By.CLASS_NAME, "btnOld").click()

    def switch_to_iframe_relatorios(self):
        sleep(1)
        iframe_relatorios = self.browser.find_element(By.ID, "frameLeft")
        self.browser.switch_to.frame(iframe_relatorios)

    def switch_to_window_relatorios(self):
        sleep(1)
        window_relatorios = self.browser.window_handles[1]
        self.browser.switch_to.window(window_relatorios)

    def switch_to_main_window(self):
        sleep(1)
        self.browser.switch_to.default_content()

    def recarregar_pagina(self):
        sleep(1)
        self.browser.refresh()

    def sair(self):
        sleep(1)
        self.browser.quit()
