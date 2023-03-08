![1678256341153](image/README/1678256341153.png)

![1678242811979](image/README/1678242811979.png)![1678242820753](image/README/1678242820753.png)

Run the following to install:

```python
pip install gli99
```

![1678242837994](image/README/1678242837994.png)![1678255311221](image/README/1678255311221.png)

```python
from gli99.tools import GifScraper

gs = GifScraper(browser="firefox")
gs.load(query="brazil",amount=5)
gs.download("D:/GifsFolder/")
```
