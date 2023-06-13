![1678306298287](image/README/1678306298287.png)

***Do NOT use this repo for professional use, this was a personal project to practice version control, web scraping, and readme design. The correct way to access GifCities.org is through its (admittedly slow) [API](https://gifcities.archive.org/api/v1/gifsearch?q=hamster).***

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
