---
title: Automatically tagging people for code review in Gerrit
description: There is a way to tag people by default for all your commits in gerrit.
date_created: 2016-11-29
---

If your gerrit workflow requires you to automatically tag people, or if you always end up tagging the same people, there is a way to tag people by default for all your commits.

To do so, edit `.git/config` to include the following lines and substitute the email with your colleague's email:

```
[remote "origin"]
 ...
 receivepack = git receive-pack --reviewer "other.reviewer@company.com"
```

