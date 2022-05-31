from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome()
delay = 60


def access_atto_solution():
    browser.get(
        "https://cloud.attodigital.com/AttoSolution/WebReporting/frmPrincipal.aspx")


def login():
    browser.get(
        "https://cloud.attodigital.com/AttoSolution/WebLogin/frmLoginAgentClient.aspx")

    login_input = browser.find_element(By.ID, "edtLogin")
    login_input.clear()
    login_input.send_keys("vik_api")

    pwd_input = browser.find_element(By.ID, "edtPws")
    pwd_input.clear()
    pwd_input.send_keys("831b29828d")

    browser.find_element(By.ID, "login-button").click()

    # if browser.find_element(By.ID, "lblError").value_of_css_property("display") == "none":
    #     browser.close()


def switch_tab():
    try:
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.ID, "btnReporting")))

        browser.find_element(By.ID, "btnReporting").click()
        sleep(1)

        atto = browser.window_handles[1]
        browser.switch_to.window(atto)
    except TimeoutException:
        print("Loading took too much time!")


def campanha_ativa():
    atto = browser.window_handles[1]
    browser.find_element(By.ID, "mnuCO").click()

    relatorio_call_history_historico()
    browser.switch_to.window(atto)

    fill_report_form()
    browser.switch_to.window(atto)

    save_report()


def relatorio_call_history_historico():
    sleep(1)
    iframe_relatorios = browser.find_element(By.ID, "frmCampOutbound_content")
    browser.switch_to.frame(iframe_relatorios)
    browser.find_element(By.ID, "myGrid-cell-0-1-box").click()
    browser.find_element(By.ID, "btnLupa").click()


def switch_to_iframe_data():
    iframe_data = browser.find_element(By.ID, "frmReportFilterShow_content")
    browser.switch_to.frame(iframe_data)


def switch_to_iframe_report():
    iframe_report = browser.find_element(By.ID, "frmReportPreview_content")
    browser.switch_to.frame(iframe_report)


def fill_report_form():
    sleep(1)
    switch_to_iframe_data()

    data = browser.find_element(By.ID, "Edit1")
    data.send_keys("12052022")

    hora_inicio = browser.find_element(By.ID, "Edit2")
    hora_inicio.send_keys("115023")

    hora_fim = browser.find_element(By.ID, "Edit3")
    hora_fim.send_keys("185023")

    ok_btn = browser.find_element(By.ID, "A1")
    ok_btn.click()


def save_report():
    sleep(1)
    switch_to_iframe_report()
    browser.find_element(By.ID, "btnSave").click()
    browser.find_element(By.ID, "divSaveCSV").click()


login()
switch_tab()
campanha_ativa()
