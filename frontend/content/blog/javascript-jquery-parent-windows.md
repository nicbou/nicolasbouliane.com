---
title: Javascript, jQuery and parent windows
description: 
date_created: 2014-03-10
---

When you open a window with `window.open`, you can access the popup's parent window using `window.opener` from the child window.

```javascript
//In the parent window
window.open('http://example.com/url'); //Opens a new window/tab with this URL

//In the opened window
window.opener.document;
```

You can perform the same requests on `window.opener.document` as you would on the `document` object:

```javascript
window.opener.document.getElementById('#tableInParent'); //Gets #tableInParent in the parent window
```

If you want to use jQuery selectors on element in the parent window, this is how you do it. In the example below, we fade out a table in the parent window:

```javascript
$(window.opener.document).find('#tableInParent').fadeOut(); //Fades out #tableInParent
```

Alternatively, you can also set the selector's scope:

```javascript
$('#tableInParent', window.opener.document).fadeOut(); //Fades out #tableInParent
```

That's it! If you want to learn jQuery properly, I highly recommend Mark Myers' "[A Smarter Way to Learn jQuery](http://amzn.to/2fAGQhN)". Mark Myers tends to write very high quality programming books with a focus on good practices.

