---
title: How to prevent Chrome from changing text color when printing
description: When you print a page with Google Chrome, the text colour changes to make it easier to read. Here's how you can prevent this in CSS.
date_created: 2017-03-07
---

Chrome has a feature that turns light text to black before printing. For instance, if you have a light gray paragraph on the page, it will print as black text.

While this feature might ensure that unoptimized pages are readable when printed, you might want to disable it so colors come out the way you intended.

To ensure that background images, background colors and text colors remain the same while printing, use the following CSS rule:

```
-webkit-print-color-adjust: exact
```

