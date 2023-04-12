---
title: How to flatten a directory on Linux and MacOS
description: How to move all the files in subdirectories to the root directory with a single terminal command.
date_created: 2018-08-30
---

If you want to flatten a directory with lots of deeply nested files (for example `./2012/06/09/images/previews/200x200/image1.jpg` becomes `./image1.jpg`), you can run this simple command:

```
find target/ -mindepth 2 -type f -exec mv -i '{}' target/ ';'
```

All the files in `target`'s subdirectories will be moved directly under `target`. If multiple files have the same name (`target/hello.txt`, `target/backup/hello.txt`, `target/hello/english/hello.txt`), you will be asked to overwrite them:

```
overwrite ./hello.txt? (y/n [n])
```

The default option is "no", so you can just hold the `Enter` key to say no to all overwrites.

