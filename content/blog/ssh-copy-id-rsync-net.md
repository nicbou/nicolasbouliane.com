---
title: ssh-copy-id does not work with rsync.net or Hetzner
description: If you tried to use ssh-copy-id with your rsync.net or Hetzner account, it probably didn't work. You're not alone.
date_created: 2021-04-09
---

You are not doing anything wrong. ssh-copy-id simply does not work with rsync.net or Hetzner. If you want to upload your public key to rsync.net to enable passwordless login, you need to follow the official instructions:

- [Hetzner instructions](https://docs.hetzner.com/robot/storage-box/backup-space-ssh-keys/)
- [rsync.net instructions](https://www.rsync.net/resources/howto/ssh_keys.html)

