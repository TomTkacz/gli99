![1678306298287](image/README/1678306298287.png)

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
