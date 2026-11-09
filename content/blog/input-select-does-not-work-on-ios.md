---
title: input.select() does not work on iOS
description: The correct way to do it is to use setSelectionRange on an already focused input.
date_created: 2015-06-29
---

The recommended method to give a text field focus and select its contents is the following:

```javascript
document.getElementById('myInput').select();
```

However, this does not work in iOS. The correct way to do it is to use `setSelectionRange` on an already focused input.

```javascript
var input = document.getElementById('myInput');
input.focus();
input.setSelectionRange(0,99999);
```

`setSelectionRange` will not work on iOS if the element doesn't have focus. Also be advised that anything revolving around giving text inputs focus [is highly unreliable](http://stackoverflow.com/questions/6287478/mobile-safari-autofocus-text-field) on mobile Safari.

