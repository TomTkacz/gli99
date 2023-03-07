# gli99 (GIF Like It's '99)

Web scraper for gifcities.org

## Installation

Run the following to install:

```python
pip install gli99
```

## Usage

```python
from gli99.tools import GifScraper

gs = GifScraper(browser="firefox")
gs.load(query="brazil",amount=5)
gs.download("D:/GifsFolder/")
```