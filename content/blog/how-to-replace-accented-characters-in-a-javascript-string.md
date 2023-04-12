---
title: How to replace accented characters in a Javascript string
description: 
date_created: 2015-07-23
---

If you are dealing with international user, you will sometimes need to replace unicode characters (éåü) with their ascii counterparts (eau).

The easiest way is to use a small library called [stringops](https://github.com/nicbou/stringops). It extends the String prototype to give your strings the `.noAccents` method. For instance, you can do `"éåü".noAccents()` and you will get `"eau"`.

The library is very lightweight, but features other useful utilities to deal with strings. The full documentation is available on [its github page](https://github.com/nicbou/stringops), along with examples.

