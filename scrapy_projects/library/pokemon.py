from scrapy_projects.library.chrome_driver_utils import make_headless_chrome_driver
import urllib.request
import os
import numpy as np

class Pokemon(object):

    def __init__(self, urls=None, base_url=None, chrome_driver_dir_path=None):
        if base_url is None:
            base_url = 'https://www.giantbomb.com'
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
        self.base_url = base_url

    def download(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_img_dir_path = output_dir + '/img'
        output_txt_dir_path = output_dir + '/txt'
        if not os.path.exists(output_img_dir_path):
            os.makedirs(output_img_dir_path)
        if not os.path.exists(output_txt_dir_path):
            os.makedirs(output_txt_dir_path)

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
                    pokemon_name = h3_text.split('.')[1].strip().lower()
                    print('found pokemon: ', pokemon_name)

                    img_elems = img_div_elem.find_elements_by_tag_name('img')
                    if len(img_elems) > 0:
                        pokemon_link = elem.get_attribute("href")
                        self.pokemon_links[pokemon_name] = pokemon_link
                        img_src = img_elems[0].get_attribute("src")
                        self.pokemon_img_links[pokemon_name] = img_src

                        img_file_path = output_img_dir_path + '/' + pokemon_name + '.png'
                        if not os.path.exists(img_file_path):
                            urllib.request.urlretrieve(img_src, img_file_path)

        for name, url in self.pokemon_links.items():
            try:
                print('extract from ', url)
                driver.get(url)
                # elems = driver.find_elements_by_xpath("//h3[@class='display-view']")
                elems = driver.find_elements_by_class_name('display-view')
                if len(elems) > 0:
                    h3_text = elems[0].text
                    print(h3_text)
                    txt_file_path = output_txt_dir_path + '/' + name + '.txt'
                    with open(txt_file_path, 'wt') as f:
                        f.write(h3_text)
            except ValueError:
                print('failed to navigate ', url)

        np.save(output_dir + '/pokemon_links.npy', self.pokemon_links)

        driver.close()


if __name__ == '__main__':
    Pokemon().download(output_dir='../demo/temp/pokemon')