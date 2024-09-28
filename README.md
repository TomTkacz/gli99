![1678306298287](image/README/1678306298287.png)

**gli99 (GIF Like Its '99) was created as an alternative to the official [GifCities API](https://gifcities.archive.org/api/v1/gifsearch?q=hamster) and was mostly just a personal practice project for Selenium WebDriver. The GifCities server is simply slow to serve image data, so either way will yield about the same result. But hey, it's Python :D**

---



![## Installation](image/README/1678242811979.png)![1678407448911](image/README/1678407448911.png)

Run the following to install:

```python
pip install gli99
```

![## Usage](image/README/1678242837994.png)![1678407713226](image/README/1678407713226.png)

```python
from gli99.tools import GifScraper

gs = GifScraper(browser="firefox")
gs.load(query="brazil",amount=5)
gs.download()
```

currently supported browsers:

* Edge
* Chrome
* Firefox

![1678475501350](image/README/1678475501350.png)

