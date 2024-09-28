<div align="center">
    <img src="https://raw.githubusercontent.com/TomTkacz/gli99/5b7e8760912ef7fd2a11ccabdca9cfc114258df6/image/README/1678306298287.png">
</div>
<br>

**gli99 (GIF Like Its '99) was created as an alternative to the official [GifCities API](https://gifcities.archive.org/api/v1/gifsearch?q=hamster) and was mostly just a personal practice project for Selenium WebDriver. The GifCities server is simply slow to serve image data, so either way will yield about the same result. But hey, it's Python :D**

---

<div>
    <img src="https://i.imgur.com/ys9tSyW.gif" height="60px"><img src="https://i.imgur.com/jJbTPjg.gif">
</div>
<hr>

Run the following to install:

```python
pip install gli99
```

<hr>
<div>
    <img src="https://i.imgur.com/Bdtlrz0.gif" height="60px"><img src="https://i.imgur.com/wjqbAoA.gif">
</div>
<hr>


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

<div align="center">
    <img src="https://i.imgur.com/GCJ3VNQ.gif">
</div>

