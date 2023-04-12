---
title: PHP preg_match failing for no reason? Blame UTF-16.
description: 
date_created: 2014-04-08
---

Recently, I've been trying to replace tabs in a document, and I was surprised when my very simple regex, `'/\t+/'`, couldn't match two tabs while Sublime Text could easily run the same find/replace without a hitch.

It turns out that the document was encoded in **UTF-16**, which PHP's `preg_*` functions doesn't support. UTF-16 adds a null byte (`\0`) after each ASCII character, which breaks your regex pattern.

All you need to do is to convert your string to UTF-8 before running your regex matcher on it:

```
$string = mb_convert_encoding($raw_string, 'UTF-8', 'UTF-16');
$string = preg_replace('/\t+/', "\t", $string); //Replaces multiple tabs with a single tab

```

It's that simple! The hardest part is to figure out why your seemingly valid string doesn't work properly before you can Google your problem.

