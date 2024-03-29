---
title: Trly.gd
description: A keyword-based search engine that redirects your search.
date_created: 2009-12-08
project_url: 
repo_url: 
featured_image: images/trlygd.png
---

Trly.gd was my first real website. It was not really a website, but a drop-in replacement for the browser's default search engine. It redirected your queries to the right search engine based on the keywords you used. For example, "images:dog" would search Google Images, "en2fr:dog" would translate words to French, "wen:dog" would search English Wikipedia and so on.

It ran untouched for over a decade. When I [rebuilt my website from scratch](/projects/personal-website-v3), I took a few minutes to rewrite [the original script](https://gist.github.com/nicbou/1cf859172710b987d4a2883f5d951aa2) in Python, enable HTTPS, and disable server logs. [It's still there](https://github.com/nicbou/nicolasbouliane.com-server/tree/main/search), serving dozens of searches every day.

![Trlygd](/images/trlygd.png)

![Trlygd2](/images/trlygd2.png)

