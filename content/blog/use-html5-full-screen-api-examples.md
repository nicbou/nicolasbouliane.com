---
title: How to use the HTML5 full screen API (with examples)
description: 
date_created: 2013-11-05
---

The new HTML5 fullscreen API allows you to build full screen web applications *very* easily.

Before we get started, there are a few things you need to know:

- Only user events (click, keyup etc.) can trigger full screen mode. This prevents pop up ads from going full screen.
- The API is supported by IE9+, Chrome and Firefox. You can see the support table on [caniuse.com](http://caniuse.com/#feat=fullscreen).
- Mobile browsers do not implement this API

With that in mind, this is how you implement a "toggle full screen" button. Place it in a click event and it will toggle full screen.

```javascript
if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement) {
    if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
    } else if (document.documentElement.mozRequestFullScreen) {
        document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.webkitRequestFullscreen) {
        document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
} else {
    if (document.cancelFullScreen) {
        document.cancelFullScreen();
    } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if (document.webkitCancelFullScreen) {
        document.webkitCancelFullScreen();
    }
}
```

