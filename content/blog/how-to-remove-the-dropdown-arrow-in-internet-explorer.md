---
title: How to remove the dropdown arrow in Internet Explorer
description: If you need this article in this year of our Lord, I hope you're okay.
date_created: 2013-09-28
---

Unlike other browsers, Internet Explorer will not fully disable a `<select>` element's style when you use the CSS3 `appearance` property. To hide the dropdown's arrow, use the following CSS line:

```css
select::-ms-expand { display: none; }
```

