---
title: How to fade images on load with jQuery
description: 
date_created: 2013-05-09
---

In this article, I will show you how to properly fade in images when the page loads using jQuery.

Although this has been covered by other blogs, most proposed solutions do not take caching into account. When returning on a page, images that were cached by the browser will not trigger jQuery's `load` event.

First, we bind the animation to the `load` of all images. Once this is done, we loop through the images using `each`, and manually trigger the `load` event for images that are already loaded because of caching.

```
$('img').hide().one("load",function(){
 $(this).fadeIn(500);
}).each(function(){
 if(this.complete) $(this).trigger("load");
});
```

In this example, we apply the effect to *all* images, which might impact performance. Replace the selector at the beginning of the snippet to limit it to the images you want to fade in.

If you want to see this jQuery snippet in effect, visit [my personal website](/). If you want to learn jQuery properly, I highly recommend Mark Myers' "[A Smarter Way to Learn jQuery](http://amzn.to/2fAGQhN)". Mark Myers tends to write very high quality programming books with a focus on good practices.

