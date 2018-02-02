# scrapy-projects

Projects using requests, BeautifulSoup, selenium, scrapy for web scraping

# Usage

### Download Thumbnails from Google Image Search

The following codes show how to download images related to "pandas" from google image search:

```python
from scrapy_projects.library.google_images import GoogleImageSearchThumbnailDownloader

downloader = GoogleImageSearchThumbnailDownloader()
downloader.download(keyword='pandas', output_dir='./temp/pandas')
```

### Download Pokemon trends CSV data from Google Trends

```python
from scrapy_projects.library.google_trends import GoogleTrendDownloader


def main():
    downloader = GoogleTrendDownloader()
    downloader.download('pokemon', output_dir='./temp/pokemon_google_trends')


if __name__ == '__main__':
    main()
```

### Download Pokemon images and description

The following codes uses selenium to download pokemon images and description:

```python
from scrapy_projects.library.pokemon import Pokemon

if __name__ == '__main__':
    Pokemon(chrome_driver_dir_path='../chromedriver').download(output_dir='./temp/pokemon')
```