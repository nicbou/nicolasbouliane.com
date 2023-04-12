---
title: Can't output OS X audio to AirPlay? Here's the fix.
description: 
date_created: 2013-12-12
---

Once in a while, I won't be able to output my Macbook's audio to my Apple TV. The solution is rather simple: you need to kill coreaudiod. You can achieve this from Activity Monitor or enter the following command in Terminal:

```bash
sudo kill `ps -ax | grep 'coreaudiod' | grep 'sbin' |awk '{print $1}'`
```

