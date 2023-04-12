---
title: Get the number of lines of code for a project
description: 
date_created: 2014-02-25
---

If you want to get the total line count for a project, you can simply combine the `find` and `wc` commands. In the example below, we get the number of lines of code for all PHP, JavaScript and CSS files under a given directory:

```
find [directory] -name '*.php' -o -name '*.js' -o -name '*.css' | xargs wc -l

```

If you want a relative number, you can use `git` commands to see how many lines were changed between two commits:

```
git diff --stat [reference commit]

```

Although line count isn't a straight measure of code quality, discovering you have cut a code base size in half without touching features is always a good feeling.

