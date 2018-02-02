from sys import platform
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

def get_chrome_driver_file_path(chrome_driver_dir_path):
    chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_win32/chromedriver.exe'
    if platform == "linux" or platform == "linux2":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_linux64/chromedriver'
    elif platform == "darwin":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_mac64/chromedriver'
    elif platform == "win32":
        chrome_driver_file_path = chrome_driver_dir_path + '/chromedriver_win32/chromedriver.exe'

    return chrome_driver_file_path


def make_headless_chrome_driver(chrome_driver_dir_path, download_folder=None):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    if download_folder is not None:
        download_folder_path = os.path.abspath(download_folder)
        print('set default download location: ', download_folder_path)
        # chrome_options.add_argument("download.default_directory=" + download_folder_path)
        prefs = {'download.default_directory': download_folder_path}
        chrome_options.add_experimental_option('prefs', prefs)

    chrome_driver_file_path = get_chrome_driver_file_path(chrome_driver_dir_path)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_file_path)

    return driver


def make_chrome_driver(chrome_driver_dir_path, download_folder=None):
    chrome_options = Options()
    if download_folder is not None:
        download_folder_path = os.path.abspath(download_folder)
        print('set default download location: ', download_folder_path)
        # chrome_options.add_argument("download.default_directory=" + download_folder_path)
        prefs = {'download.default_directory': download_folder_path}
        chrome_options.add_experimental_option('prefs', prefs)
    # chrome_options.add_argument("--headless")

    chrome_driver_file_path = get_chrome_driver_file_path(chrome_driver_dir_path)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_file_path)

    return driver