---
title: Multiple git stashes
description: Did you know git can keep multiple stashes? Here's how to do it.
date_created: 2015-07-15
---

Did you know git can keep multiple stashes? If you use `git stash` and `git stash apply`, you might be tempted to think there is a single stash, but you can restore older stashes, and thus stash multiple items.

To see your previous stashes, use `git stash list`. You will get a result like this:

```
stash@{0}: WIP on master: 6c483e2 Updated location.search to use empty string instead of null
stash@{1}: WIP on master: 6c483e2 Updated location.search to use empty string instead of null
stash@{2}: WIP on master: 142e661 Removed middle state for the search results panel
stash@{3}: WIP on master: 0e65041 Added spinner to search
stash@{4}: WIP on master: 723eef5 Put the search query in the search service
...
```

To restore a particular stash, use `git stash apply stash@{0}` and replace `0` with the index of the stash you wish to restore.

Use `git stash clear` to erase all your stashed changes.

