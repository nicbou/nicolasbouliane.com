---
title: Create a global .gitignore in git
description: How to ignore files in all git repositories on your machine. It's a good way to make git ignore .DS_Store and other system files.
date_created: 2014-01-20
---

Are you tired of adding `.DS_Store`, `.idea` and other files to the .gitignore of all of your projects?

Git lets you specify a universal .gitignore file to ignore them once and for all. It's a rather simple command:

```bash
git config --global core.excludesfile /path/to/global/.gitignore
```

Pretty simple, isn't it?

