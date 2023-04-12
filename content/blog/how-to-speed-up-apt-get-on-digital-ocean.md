---
title: How to speed up apt-get on Digital Ocean
description: For some reason, downloading packages using apt-get install was unusually slow on DigitalOcean this week. The fix was really easy.
date_created: 2016-03-25
---

For some reason, downloading packages using `apt-get install` was unusually slow on DigitalOcean this week, barely exceeding 4kbps. Since DigitalOcean droplets are configured to download packages from mirrors.digitalocean.com, all I had to do was to revert them to the default Ubuntu sources using these two commands:

```bash
sudo sed -i "s/mirrors.digitalocean/archive\.ubuntu/g" /etc/apt/sources.list
sudo apt-get update
```

Downloads are now as fast as they should be.

