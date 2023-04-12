---
title: Zepto.js and the :selected and :checked selectors
description: 
date_created: 2013-07-25
---

If you switched from jQuery to its slightly anemic cousin, Zepto.js, you might have noticed that it doesn't support two rather useful selectors, :selected and :checked.

Fortunately, it is fairly easy to compensate for it.

First, define the following two functions:

```
var checked = function(){ return this.checked; }
var selected = function(){ return this.selected; }

```

Once this is done, you can properly filter elements using `.filter()` and `.not()`, which are present in both jQuery and Zepto.js

```
// Equivalent to $('.radiobutton:checked')
$('.radiobutton').filter(checked);

// Equivalent to $('.dropdown:selected')
$('.dropdown').filter(selected);

```

These functions will only return selected/checked elements.

