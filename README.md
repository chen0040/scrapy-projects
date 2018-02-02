# scrapy-projects

Projects using requests, BeautifulSoup, selenium, scrapy for web scraping

# Usage

The library of the various scrappers are contained in the [library](scrapy_projects/library) folder

The demo codes on how to crawling various web data sources can be found in the [demo](scrapy_projects/demo) folder

To run the demo codes in PyCharm, say [demo/google_trend_download.py], right-click the python file in PyCharm and click
"Run google_trend_download" option in the pop-up menu.

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