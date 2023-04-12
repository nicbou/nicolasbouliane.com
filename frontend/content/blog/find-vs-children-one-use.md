---
title: .find() vs. .children(): which one should you use?
description: 
date_created: 2014-04-22
---

jQuery offers two functions to find children in an element: `.find()` and `.children()`. `.find()` will look through all children of an element while `.children()` will only look at immediate children.

```
<ul>
 <li>
 <p></p>
 </li>
 <li>
 <p></p>
 </li>
 <li>
 <p></p>
 </li>
</ul>
```

In the snippet above, `$('ul').children('p')` wouldn't return anything, while `$('ul').find('p')` would return all three paragraph blocks.

In terms of performance, `.find()` **is faster** than `.children()` in most cases, since it uses native browser methods instead of JavaScript.

Here is [a performance test](http://jsperf.com/jquery-children-vs-find/3) that compares `.find()` and `.children()`.

That was it! If you want to learn jQuery properly, I highly recommend Mark Myers' "[A Smarter Way to Learn jQuery](http://amzn.to/2fAGQhN)". Mark Myers tends to write very high quality programming books with a focus on good practices.

