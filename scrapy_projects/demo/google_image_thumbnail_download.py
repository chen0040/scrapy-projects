from scrapy_projects.library.google_images import GoogleImageSearchThumbnailDownloader

def main():
    downloader = GoogleImageSearchThumbnailDownloader()
    categories = ['chair', 'bed', 'table', 'cabinet', 'sofa', 'lighting', 'wardrobe']
    for category in categories:
        downloader.download(keyword=category, output_dir='../demo/temp/' + category)


if __name__ == '__main__':
    main()