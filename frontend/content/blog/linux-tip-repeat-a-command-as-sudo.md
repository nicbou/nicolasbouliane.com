---
title: Linux tip: repeat a command as sudo
description: 
date_created: 2013-09-28
---

When you run a command in the terminal, and realize it requires superuser permissions, use the following command to re-run the command as superuser:

```
sudo !!

```

Here is an example scenario:

```
apt-get install myapplication
(permission denied)
sudo !!

```

The best part is that you can use this to prefix your command with *anything*. In the example below, I forgot to put `cd` in front of my file path.

```
nicolas@nicolas-Revo ~ $ Backup
No command 'Backup' found, did you mean:
 Command 'rackup' from package 'ruby-rack' (universe)
 Command 'backup' from package 'openafs-client' (universe)
 Command 'packup' from package 'packup' (universe)
Backup: command not found

nicolas@nicolas-Revo ~ $ cd !!

nicolas@nicolas-Revo ~/Backup $ 
```

