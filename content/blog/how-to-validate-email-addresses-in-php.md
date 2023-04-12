---
title: How to validate email addresses in PHP
description: The correct and the wrong ways to validate an email address in PHP
date_created: 2013-04-04
---

How to validate email addresses in PHP

This regex will match email adresses. However, it's not bulletproof. Emails such as `n@n.n` or `____@--...` would still pass validation.

```
/^([a-z0-9_\.\+-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/

```

If you are using PHP, you can also use `filter_var()` and save yourself some headaches. As illustrated [here](http://codepad.org/Lz5m2S2N), it correctly validates most addresses.

```
filter_var('test@test.com', FILTER_VALIDATE_EMAIL); //Returns true if email is valid, false otherwise
```

