from scrapy_projects.library.google_images import GoogleImageSearchThumbnailDownloader

def main():
    downloader = GoogleImageSearchThumbnailDownloader()
    downloader.download(keyword='cute pandas', output_dir='../demo/temp/cute_pandas')


if __name__ == '__main__':
    main()