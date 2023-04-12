---
title: Fix garbled file names in SMB shares
description: If you have files in your SMB networked folders that look like this: TRZB4~J.mp4, there is a very easy fix to get the original file names.
date_created: 2014-06-23
---

If you have files in your SMB networked folders that look like this: `TRZB4~J.mp4`, there is a very easy fix to get the original file names.

Open your `smb.conf` file (usually at `/etc/samba/smb.conf`) and add the following line under `[global]`:

```
mangle case = no
mangled names = no
```

Once this is done, enter the following command in your terminal:

```
sudo service samba2 restart
```

Names are mangled to make them compatible with older operating systems, but this absolutely shouldn't be a problem that you will face at home.

