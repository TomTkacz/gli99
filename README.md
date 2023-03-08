![1678240674995](image/README/1678240674995.png)

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
