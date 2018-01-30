import requests
from bs4 import BeautifulSoup
import urllib.request
import os

class GoogleImageDownloader(object):
    def __init__(self, base_url=None):
        self.page_size = 10
        if base_url is None:
            base_url = 'https://www.google.com/search'
        self.base_url = base_url

    def download(self, keyword, output_dir):

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        url = self.base_url + '?q=' + keyword + '&dcr=0&source=lnms&tbm=isch&sa=X&biw=1680&bih=919'
        page = requests.get(url).text

        soup = BeautifulSoup(page, 'html.parser')
        for raw_link in soup.find_all('a'):
            link = raw_link.get('href')
            # print(link)
            if type(link) == str and 'imgurl' in link:
                # print the part of the link that is between "=" and "&" (which is the actual url of the image,
                print(link.split('=')[1].split('&')[0])

        counter = 1
        for raw_img in soup.find_all('img'):
            link = raw_img.get('src')
            if link and type(link) == str and 'images' in link:
                print('downloading image from ', link)
                urllib.request.urlretrieve(link, output_dir + '/' + keyword + str(counter) + '.png')
                counter += 1


def main():
    downloader = GoogleImageDownloader()
    downloader.download(keyword='pandas', output_dir='../demo/temp/pandas')


if __name__ == '__main__':
    main()