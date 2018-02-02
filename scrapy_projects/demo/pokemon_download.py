from scrapy_projects.library.pokemon import Pokemon

if __name__ == '__main__':
    Pokemon().download(output_dir='./temp/pokemon')