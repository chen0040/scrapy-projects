from scrapy_projects.library.pokemon import Pokemon

if __name__ == '__main__':
    Pokemon(chrome_driver_dir_path='../chromedriver').download(output_dir='./temp/pokemon')