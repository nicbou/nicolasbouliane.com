---
title: How to change crontab's location
description: For a reason or another, you might one to change your crontab's location. Here's how.
date_created: 2013-09-28
---

For a reason or another, you might one to change your crontab's location. For instance, you might want to move it under a version-controlled directory or keep it under your backed up directories. When I reinstalled my home server, I've put all of my essential scripts under a directory on another partition to make distro upgrades easier.

The line below will change the crontab location for user *nicolas*

```bash
crontab -u nicolas /my/crontab/path
```

