---
title: Getting the hash of the first commit in git
description: Get one commit, and show its SHA1.
date_created: 2014-02-05
---

If you want to know what your oldest git commit is, use the following command to return its hash:

```bash
git rev-list HEAD | tail -n 1
```

You can then use `git show` to find the commit date, author and message:

```bash
git show --quiet [your hash]
```

To show the diff for that first commit, remove the `--quiet` flag.

