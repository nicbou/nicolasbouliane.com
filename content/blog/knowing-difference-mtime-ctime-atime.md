---
title: Knowing the difference between mtime, ctime and atime
description: 
date_created: 2014-03-01
---

If you are dealing with files, you might wonder what the difference is between `mtime`, `ctime` and `atime`.

`mtime`, or modification time, is when the file was last modified. When you change the *contents* of a file, its mtime changes.

`ctime`, or change time, is when the file's property changes. It will always be changed when the mtime changes, but also when you change the file's permissions, name or location.

`atime`, or access time, is updated when the file's contents are read by an application or a command such as `grep` or `cat`.

The easiest way to remember which is which is to read their alphabetical order:

- `Atime` can be updated alone
- `Ctime` will update `atime`
- `Mtime` will update both `atime` and `ctime`.

