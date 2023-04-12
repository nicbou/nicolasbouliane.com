---
title: How to enable root login on Ubuntu
description: This lets you SSH into your Ubuntu server as root.
date_created: 2021-04-30
---

This is how you can login as root with a Ubuntu server:

1. Run `sudo passwd root` to enable to root account and give it a password.
2. Edit `/etc/ssh/sshd_config`, and add the line `PermitRootLogin yes`.
3. Restart sshd with `sudo service sshd restart`.

You can now SSH into your machine as root.

