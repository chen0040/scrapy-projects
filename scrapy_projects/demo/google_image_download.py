from scrapy_projects.library.google_images import GoogleImageDownloader

def main():
    downloader = GoogleImageDownloader()
    downloader.download(keyword='pandas', output_dir='../demo/temp/pandas')


if __name__ == '__main__':
    main()