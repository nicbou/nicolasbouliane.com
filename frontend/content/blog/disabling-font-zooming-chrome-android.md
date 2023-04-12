---
title: Disabling font zooming in Chrome on Android
description: 
date_created: 2014-04-08
---

If you are here, you have probably tried disabling font zooming by using `-webkit-text-size-adjust:100%` and discovered it didn't work.

Chrome conveniently ignores this non-standard property, so you need to use an inconvenient hack to disable what is called **font boosting** by adding the following line to your CSS file:

```css
html * {max-height:1000000px;}
```

Your fonts should then appear as they should even on Android devices, and the zoom will work properly.

