---
title: How to prevent Safari from resizing text in iOS
description: How to prevent Safari from resizing text in iOS
date_created: 2013-05-29
---

By default, rotating the iPhone's screen will resize the font in mobile Safari. Although this can be useful for desktop websites, it can easily break a beautiful mobile design.

All you need to do is to set the following CSS attribute on the `body` element:

```
-webkit-text-size-adjust: none;
```

This will prevent webkit browsers (Safari included) from messing with your font sizes.

