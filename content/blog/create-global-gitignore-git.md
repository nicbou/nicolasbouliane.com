---
title: Create a global .gitignore in git
description: 
date_created: 2014-01-20
---

Are you tired of adding `.DS_Store`, `.idea` and other files to the .gitignore of all of your projects?

Git lets you specify a universal .gitignore file to ignore them once and for all. It's a rather simple command:

```
git config --global core.excludesfile /path/to/global/.gitignore
```

Pretty simple, isn't it?

