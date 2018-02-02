from scrapy_projects.library.chrome_driver_utils import make_headless_chrome_driver


class GoogleTrendDownloader(object):
    def __init__(self, base_url=None, chrome_driver_dir_path=None):
        if chrome_driver_dir_path is None:
            chrome_driver_dir_path = '../chromedriver'
        if base_url is None:
            base_url = 'https://trends.google.com/trends/'
        self.base_url = base_url
        self.chrome_driver_dir_path = chrome_driver_dir_path

    def download(self, keywords, date=None):
        if date is None:
            date = 'now%201-d'

        browser = make_headless_chrome_driver(self.chrome_driver_dir_path)
        url = self.base_url + '/explore#q=' + keywords + '&date=' + date
        browser.get(url)



def main():
    downloader = GoogleTrendDownloader()
    downloader.download('google')


if __name__ == '__main__':
    main()