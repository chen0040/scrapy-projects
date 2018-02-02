from scrapy_projects.library.chrome_driver_utils import make_headless_chrome_driver

class Pokemon(object):

    def __init__(self, urls=None, chrome_driver_dir_path=None):
        if urls is None:
            urls = [
                'https://www.giantbomb.com/profile/wakka/lists/the-150-original-pokemon/59579/',
                'https://www.giantbomb.com/profile/wakka/lists/the-150-original-pokemon/59579/?page=2'
            ]
        if chrome_driver_dir_path is None:
            chrome_driver_dir_path = '../chromedriver'
        self.urls = urls
        self.chrome_driver_dir_path = chrome_driver_dir_path

    def download(self):
        driver = make_headless_chrome_driver(self.chrome_driver_dir_path)

        for url in self.urls:
            driver.get(url)
            elems = driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                img_elems = elem.find_elements_by_class_name("imgboxart")
                if len(img_elems) > 0:
                    print(elem.get_attribute("href"))

        driver.close()


if __name__ == '__main__':
    Pokemon().download()