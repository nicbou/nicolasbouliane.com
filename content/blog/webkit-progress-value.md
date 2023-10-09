---
title: Why ::-webkit-progress-value has no effect
description: Can't change your progress bar colours in Chrome and Safari? It's probably because of this Chromium bug
date_created: 2023-10-09
categories: reference
    technology
---

You can use the `::-webkit-progress-value` selector to style `<progress>` bars in Chrome and Safari.

If the selector does not work and your CSS styles have no effect, it's probably because of [this Chromium bug](https://bugs.chromium.org/p/chromium/issues/detail?id=81705). The `::-webkit-progress-value` selector does not work if there are other selectors around it:

```css
::-webkit-progress-bar, ::-moz-progress-bar{
    /* Does not work */
}

progress::-webkit-progress-bar{
    /* Does not work */
}

::-webkit-progress-bar{
    /* Works */
}
```