---
title: Push a git to multiple repositories at once
description: 
date_created: 2014-01-20
---

If you want to push a git to several remote repositories at one, use this simple command:

```
git remote set-url --add --push [repository] [url]

```

For example, here's how I add Ignition's GitHub repo to origin:

```
git remote set-url --add --push origin https://github.com/nicbou/Ignition
```

