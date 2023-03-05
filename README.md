# gli99 (Gif Like It's '99)

Web scraper for gifcities.org

## Installation

Run the following to install:

```python
pip install gli99
```

## Usage

```python
from gli99 import GifScraper

gs = GifScraper(browser="firefox")
gs.load(query="brazil",amount=5)
gs.download("D:/GifsFolder/")
```

# Developing gli99

To install gli99, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```