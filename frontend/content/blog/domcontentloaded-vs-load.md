---
title: Halving All About Berlin's load time
description: A tiny change made the JavaScript code on All About Berlin load twice as fast.
date_created: 2021-10-25
---

I spend a lot of time making All About Berlin fast. It's just text on a page; it should be fast. Still, while the pages load instantly, the bits of JavaScript functionality took an extra second to load. It's hardly noticeable, but hardly justifiable.

When I profiled the page, I found the culprit: the `load` event took 750 milliseconds to fire. Nothing happened before that event fired. Once `load` fired, the actual functionality loaded in about 10 milliseconds.

The `load` event is fired after everything on the page is loaded, including stylesheets and images. Instead, I used the `DOMContentLoaded` event, which is fired as soon as the DOM is ready. It's the event jQuery's `$(document).ready()` binds to. That shaved about 400 milliseconds off the page load time.

[As the MDN page says](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event), it's a common mistake. People use load when`DOMContentLoaded` is more appropriate. On a slow internet connection, this makes a big difference. Images can take a while to load, but they shouldn't hold the rest of the functionality back.

