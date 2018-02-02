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
        self.pokemon_links = dict()
        self.pokemon_img_links = dict()

    def download(self):
        driver = make_headless_chrome_driver(self.chrome_driver_dir_path)

        for url in self.urls:
            driver.get(url)
            elems = driver.find_elements_by_xpath("//a[@href]")
            for elem in elems:
                img_div_elems = elem.find_elements_by_class_name("imgboxart")
                h3_elems = elem.find_elements_by_tag_name('h3')
                if len(img_div_elems) > 0 and len(h3_elems) > 0:
                    img_div_elem = img_div_elems[0]
                    h3_text = h3_elems[0].text
                    pokemon_name = h3_text.split('.')[1].trim()
                    print('found pokemon: ', pokemon_name)
                    img_elems = img_div_elem.find_elements_by_tag_name('img')
                    if len(img_elems) > 0:
                        pokemon_link = elem.get_attribute("href")
                        self.pokemon_links[pokemon_name] = pokemon_link
                        img_src = img_elems[0].get_attribute("src")
                        self.pokemon_img_links[pokemon_name] = img_src

        driver.close()


if __name__ == '__main__':
    Pokemon().download()