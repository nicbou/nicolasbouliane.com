---
title: Fixing "/usr/bin/env: node: No such file or directory"
description: After a fresh install of npm and bower, you may run into this error while running bower install. Here's the fix.
date_created: 2015-06-24
---

After a fresh install of npm and bower, you may run into the following error while running `bower install`:

```
/usr/bin/env: node: No such file or directory
```

The fix on Ubuntu is very simple:

```bash
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

