# scrapy-projects

Projects using requests, BeautifulSoup, scrapy for web scraping

# Usage

### Download Thumbnails from Google Image Search

The following codes show how to download images related to "pandas" from google image search:

```python
from scrapy_projects.library.google_images import GoogleImageSearchThumbnailDownloader

downloader = GoogleImageSearchThumbnailDownloader()
downloader.download(keyword='pandas', output_dir='../demo/temp/pandas')
```
