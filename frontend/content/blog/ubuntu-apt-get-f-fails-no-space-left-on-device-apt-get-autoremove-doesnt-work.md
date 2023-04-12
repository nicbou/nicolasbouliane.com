---
title: Ubuntu: apt-get -f fails, "no space left on device", apt-get autoremove doesn't work.
description: How to fix this pesky error when running apt-get install or some other command.
date_created: 2018-02-05
---

After getting this issue on two different servers, I thought I'd write a tutorial for everyone else.

## What's the problem?

First, you try to install some packages, either with `apt-get install` or `apt-get update`. For some reason, it fails with an error like this one:

```
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 linux-image-extra-4.4.0-112-generic : Depends: linux-image-4.4.0-112-generic but it is not going to be installed
 linux-image-extra-4.4.0-93-generic : Depends: linux-image-4.4.0-93-generic but it is not going to be installed
 linux-image-generic : Depends: linux-image-4.4.0-112-generic but it is not going to be installed
 Recommends: thermald but it is not going to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
```

So you type `apt-get -f install`, and that fails too, this time with an error like this one:

```
Unpacking linux-image-4.4.0-112-generic (4.4.0-112.135) ...
dpkg: error processing archive /var/cache/apt/archives/linux-image-4.4.0-112-generic_4.4.0-112.135_amd64.deb (--unpack):
 cannot copy extracted data for './boot/System.map-4.4.0-112-generic' to '/boot/System.map-4.4.0-112-generic.dpkg-new': failed to write (No space left on device)
No apport report written because the error message indicates a disk full error
 dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
...
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

You do a bit of research and find something about running out of inodes, so you type `df -i`, but you are using under 10% of the inodes on all devices. Another post suggests running `apt-get autoremove`, but that gives you the same error message as before:

```
You might want to run 'apt-get -f install' to correct these.
The following packages have unmet dependencies:
 linux-image-extra-4.4.0-112-generic : Depends: linux-image-4.4.0-112-generic but it is not installed
 linux-image-extra-4.4.0-93-generic : Depends: linux-image-4.4.0-93-generic but it is not installed
 linux-image-generic : Depends: linux-image-4.4.0-112-generic but it is not installed
 Recommends: thermald but it is not installed
E: Unmet dependencies. Try using -f.
```

So what's the f\*\*\*ing deal?!

## How to solve that problem

Long story short, **you don't have enough space to fit the new Linux kernel, so you have to delete some of the old ones**. You can delete those manually, but it's a long, tricky manual process, and if you're like me, you only understand half of what's going on and you just want the damn thing to work.

You might have found [this solution](http://www.mogilowski.net/lang/en-us/2014/04/14/remove-old-kernel-packages-from-ubuntu/) or a variant of it, but once more you'll get one of the error messages above:

```
Unmet dependencies. Try 'apt-get -f install' with no packages
```

Well, you were almost there! All you need is to use `dpkg` instead of `apt-get purge`.

Before you try that, run this command to see which packages will be removed. This command has no side effects and will not delete anything:

```
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d'
```

Make sure that your current kernel version is not in that list. You can see your kernel version by running `uname -a`.

Once you are sure that you want to delete these kernel files, run this command to run `dpkg --remove` on each of them:

```
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs dpkg --remove
```

After that, you can run `apt-get -f install` without problems, then do whatever you wanted to do in the first place. See, Linux isn't that complicated!

## Help! That didn't work!

If you run into an error like this one:

```
gzip: stdout: No space left on device
E: mkinitramfs failure cpio 141 gzip 1
...
Errors were encountered while processing:
 linux-image-extra-4.4.0-31-generic
 linux-image-extra-4.4.0-47-generic
 linux-image-extra-4.4.0-75-generic
 linux-image-extra-4.4.0-79-generic
 linux-image-extra-4.4.0-81-generic
 linux-image-extra-4.4.0-83-generic
 linux-image-extra-4.4.0-87-generic
 linux-image-extra-4.4.0-89-generic
```

...don't panic! *Some* of the kernels will likely removed, so you can run `apt-get -f autoremove` to clear up some space, and then you can run the long command above again.

## tl;dr

```
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs dpkg --remove
apt-get -f install
```

