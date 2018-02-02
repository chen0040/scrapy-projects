from sys import platform
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_chrome_driver_file_path(chrome_driver_dir_path):
    chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_win32/chromedriver.exe'
    if platform == "linux" or platform == "linux2":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_linux64/chromedriver'
    elif platform == "darwin":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_mac64/chromedriver'
    elif platform == "win32":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_win32/chromedriver.exe'

    return chrome_driver_file_path


def make_headless_chrome_driver(chrome_driver_dir_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    chrome_driver_file_path = get_chrome_driver_file_path(chrome_driver_dir_path)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_file_path)

    return driver


def make_chrome_driver(chrome_driver_dir_path):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    chrome_driver_file_path = get_chrome_driver_file_path(chrome_driver_dir_path)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_file_path)

    return driver