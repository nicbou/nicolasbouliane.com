---
title: Using CSS3 transforms and calc() in Internet Explorer
description: Although CSS calc sizes are supported in Internet Explorer 10 and above, they do not work when used in transform attributes. Here's the fix.
date_created: 2015-06-16
---

Although CSS `calc` sizes [are supported in Internet Explorer 10 and above](http://caniuse.com/#search=calc), they do not work when used in `transform` attributes. For instance, `transform: translate(0, calc(100% - 10px));` does not work in Internet Explorer.

To work around this, you can chain transforms. For instance, the following statements are equivalent:

```
transform: translate(0, calc(100% - 10px)); //Does not work in IE
transform: translate(0, 100%) translate(0, -10px); //Works in IE
```

It's that simple!

