---
title: Fixing the "protocol error: bad pack header" error in git
description: In my case, it was because I pulled a corrupted remote Gerrit repository, and tried to push the corrupted data back to the fixed remote.
date_created: 2016-12-06
---

When trying to push in git, you might get the following error message:

```
fatal: internal server error
remote: internal server error
fatal: protocol error: bad pack header
```

In my case, it was because I pulled a corrupted remote Gerrit repository, and tried to push the corrupted data back to the fixed remote. Everyone who had pulled the corrupted repository also ran into the same error.

Fortunately, the fix is really easy. All you have to do is run those four commands:

```
cp .git/config .git/config.backup
git remote remove origin
mv .git/config.backup .git/config
git fetch
```

This fix comes from [Jordan Klassen](https://coderwall.com/p/h5_fya/fixing-a-corrupt-local-git-repository).

