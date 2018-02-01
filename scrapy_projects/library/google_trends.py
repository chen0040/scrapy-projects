from selenium import webdriver


class GoogleTrendDownloader(object):
    def __init__(self, base_url=None):
        if base_url is None:
            base_url = 'https://trends.google.com/trends/'
        self.base_url = base_url

    def download(self, keywords, user_agent=None, date=None):
        if user_agent is None:
            user_agent = 'Mozilla/5.0'
        if date is None:
            date = 'now%201-d'

        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=' + user_agent + ' ')
        browser = webdriver.Chrome(chrome_options=options)

        url = self.base_url + '/explore#q=' + keywords + '&date=' + date
        browser.get(url)


def main():
    downloader = GoogleTrendDownloader()
    downloader.download('google')


if __name__ == '__main__':
    main()