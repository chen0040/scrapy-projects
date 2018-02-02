from scrapy_projects.library.chrome_driver_utils import make_chrome_driver
import time
import os

class GoogleTrendDownloader(object):
    def __init__(self, base_url=None, chrome_driver_dir_path=None):
        if chrome_driver_dir_path is None:
            chrome_driver_dir_path = '../chromedriver'
        if base_url is None:
            base_url = 'https://trends.google.com/trends'
        self.base_url = base_url
        self.chrome_driver_dir_path = chrome_driver_dir_path

    def download(self, keywords, output_dir, date=None):
        if date is None:
            date = 'now%201-d'

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        saved_folder_path = output_dir + '/' + keywords

        if not os.path.exists(saved_folder_path):
            os.makedirs(saved_folder_path)

        browser = make_chrome_driver(self.chrome_driver_dir_path, download_folder=saved_folder_path)
        url = self.base_url + '/explore?q=' + keywords + '&date=' + date
        print('getting url: ', url)

        browser.get(url)

        time.sleep(3)

        buttons = browser.find_elements_by_tag_name("button")
        for button in buttons:
            button_class = button.get_attribute('class')
            i_elements = button.find_elements_by_tag_name('i')
            if 'export' in button_class and len(i_elements) > 0:
                print('clicking export button: ', button.get_attribute('title'))
                print('executing: ', button.get_attribute('ng-click'))
                button.click()

        browser.close()



def main():
    downloader = GoogleTrendDownloader()
    downloader.download('google', output_dir='../demo/temp/google_trends')


if __name__ == '__main__':
    main()