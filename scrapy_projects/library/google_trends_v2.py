from requests_html import HTMLSession


class PInterestImageSearch(object):

    def __init__(self):
        self.url = 'https://trends.google.com/trends'
        self.session = HTMLSession()

    def download_images(self, keywords, date=None):
        if date is None:
            date = 'now%201-d'

        r = self.session.get(self.url + '/explore?q=' + keywords + '&date=' + date)
        r.html.render()
        for img in r.html.find('button'):
            print(img)
        for link in r.html.find('a'):
            print(link)


if __name__ == '__main__':
    pi = PInterestImageSearch()
    pi.download_images(keywords='test')
