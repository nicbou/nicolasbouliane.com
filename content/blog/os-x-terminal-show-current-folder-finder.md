---
title: OS X Terminal: Open the current folder in Finder
description: A nifty little command that opens the current terminal directory in a finder window.
date_created: 2013-11-15
---

If you use the OS X terminal, you are probably familiar with the `open` command. Essentially, it opens the given file with the default application, or with the application specified with the `-a` parameter. For example, `open hello.txt` will open hello.txt using TextEdit or your default text editor.

You can also use this command to open the current directory in Finder:

```bash
open .
```

This also works with any directory you pass as an argument:

```bash
open /Library
```

This is a great way to save time on operations that are easier to perform with a graphical interface, and to access hidden folders easily. Another way to do this is to use *Go > Go to folder* (Cmd+Shift+G) in Finder.

