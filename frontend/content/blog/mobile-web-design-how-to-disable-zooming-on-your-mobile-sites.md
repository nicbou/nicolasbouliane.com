---
title: Mobile web design: how to disable zooming on your mobile sites
description: When you are making a mobile website, you might want to disable sideways scrolling and zooming. Here's how you do it.
date_created: 2013-06-02
---

When you are making a mobile website, you might want to disable sideways scrolling and zooming. Although I wouldn't personally recommend disabling zooming, it's easily done.

In your `head` tag, insert the following meta tag:

```
<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />

```

This tag is recognized by all major browsers, including Chrome on Android and Safari on iOS.

