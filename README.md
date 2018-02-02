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

### Download Pokemon images and description

The following codes uses selenium to download pokemon images and description:

```python
from scrapy_projects.library.pokemon import Pokemon

if __name__ == '__main__':
    Pokemon().download(output_dir='./temp/pokemon')
```