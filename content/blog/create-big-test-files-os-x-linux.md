---
title: How to create big test files in OS X and Linux
description: If you need a big file for testing purposes, use mkfile.
date_created: 2014-01-30
---

If you need to have large files to test your application, there is a command in OS X and Linux that allows you to create a file of an arbitrary size.

We already know that you can create an empty file by using `touch`:

```bash
touch myfile.ext
```

You can also create files with a preset size with the `mkfile` command:

```bash
mkfile -n 2g my2gbfile.ext
```

That's it! You now have a 2 gigabyte file called my2gbfile.ext in your directory.

