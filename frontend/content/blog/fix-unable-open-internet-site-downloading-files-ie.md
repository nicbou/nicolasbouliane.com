---
title: Fix "Unable to open this Internet site" when downloading files in IE
description: 
date_created: 2014-03-17
---

Have you received the following error while downloading an attachment in Internet Explorer?

> Unable to download [file] from [domain].
> 
> Unable to open this Internet site. The requested site is either unavailable or cannot be found. Please try again later.

This seemingly random bug is fortunately pretty easy to fix. Nake sure you set the following line in your HTTP headers:

```
Cache-Control:private

```

That's it. One more tiny fix to a seemingly random problem.

