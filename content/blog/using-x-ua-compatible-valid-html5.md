---
title: Using X-UA-Compatible with valid HTML5
description: 
date_created: 2014-04-04
---

If you were using `<meta http-equiv="X-UA-Compatible" content="IE=edge" />` to force IE to use the most recent rendering engine and disable compatibility mode, you might have discovered that it's not a valid HTML5 meta tag.

The easiest way to solve it is to use `.htaccess` or your Apache config to always send X-UA-Compatible in the HTTP headers. Add the following line to your `.htaccess` file:

```
Header set X-UA-Compatible "IE=edge"

```

With that set, you won't see that pesky compatibility mode again, and your HTML5 will validate.

