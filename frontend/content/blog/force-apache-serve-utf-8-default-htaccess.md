---
title: How to force Apache to serve UTF-8 by default in .htaccess
description: 
date_created: 2014-02-14
---

If you want to serve all text files as unicode by default, add the following line to your .htaccess:

```
AddDefaultCharset utf-8
```

You can also set the encoding on individual file types using `AddCharset`:

```
AddCharset utf-8 .html .css .js .php
```

