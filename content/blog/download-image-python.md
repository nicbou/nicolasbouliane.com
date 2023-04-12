---
title: How to download an image in Python
description: 
date_created: 2014-01-29
---

Sometimes, simple problems have simple solutions. Downloading images with Python is one of those simple problems. Nonetheless, here's a simple snippet that shows you how to do it:

```python
import urllib
urllib.urlretrieve("http://www.nicolasbouliane.com/pictures/0001.jpg", "my_picture_file.jpg")
```
