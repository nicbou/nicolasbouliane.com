---
title: How to show grep results results in context
description: If you are using grep, you might want to give your results a little context and see lines before and after.
date_created: 2013-06-28
---

If you are using grep, you might want to give your results a little context and see lines before and after.

The -C argument lets you specify the number of lines to show before and after the result. For instance, `grep my_string my_file.txt -C 2` will show two lines before and two lines after your result.

