from scrapy_projects.library.google_trends import GoogleTrendDownloader


def main():
    downloader = GoogleTrendDownloader()
    downloader.download('pokemon', output_dir='./temp/pokemon_google_trends')


if __name__ == '__main__':
    main()