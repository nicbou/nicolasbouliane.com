---
title: How to use different CSS styles depending on screen orientation
description: Most modern browsers support the orientation media attribute, which allows you to define specific styles for devices in portrait or landscape mode
date_created: 2013-05-09
---

Most modern browsers support the orientation media attribute, which allows you to define specific styles for devices in portrait or landscape mode. This is especially useful when designing websites for mobile devices.

Here is how you use the orientation media selectors:

```css
@media screen and (orientation:portrait) {
    /* Portrait styles */
}

@media screen and (orientation:landscape) {
    /* Landscape styles */
}
```

This selector is supported by all modern mobile browsers.

