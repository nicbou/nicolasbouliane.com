---
title: Deleting directories while preserving symlinks
description: At work, we needed to replace a pre-existing folder with a symlink. Here's how we did it.
date_created: 2016-03-09
---

At work, we needed to **replace a pre-existing folder with a symlink**. We wanted to symlink the user's `.git/hooks` folder to `../build/git-hooks` every time the script was run.

We wanted to delete `.git/hooks` if it existed and replace it with a symlink, but we also wanted to avoid deleting `../build/git-hooks`'s contents by accident if the symlink already existed.

Using `rm .git/hooks` was not possible. If `.git/hooks` was already a symlink, it would be deleted and we could simply recreate it. Perfect! However, if `.git/hooks` was a non-empty directory (it contains examples by default), it would not be deleted, and the symlink could not be created.

Using `rm -r .git/hooks` was also impossible. If `.git/hooks` was already symlinked, the `-r` flag would delete the contents of `../build/git-hooks`.

This is how we solved the problem:

```
#!/bin/bash
set -e # Script exits with 1 on error

git_hooks_dir=".git/hooks"
link_to="../build/git-hooks"

# Safely delete the folder or symlink
if [[ -L $git_hooks_dir ]];
then
 # Folder already symlinked. Recreate symlink in case the directory changed.
 rm -f $git_hooks_dir
else
 # Possibly an existing, non-empty folder. 
 rm -rf $git_hooks_dir
fi

# Create the symlink
ln -sf $link_to $git_hooks_dir
```

