---
title: How to push all branches in git
description: 
date_created: 2014-01-27
---

If you want to push all branches in your repository when you type `git push`, type the following commands:

```
git config --add remote.origin.push '+refs/heads/*:refs/heads/*'
git config --add remote.origin.push '+refs/tags/*:refs/tags/*'
```

This will tell git to push everything including branches that were never pushed when you don't specify what to push.

