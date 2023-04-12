---
title: How to edit commits and erase mistakes from git history
description: Here's what to do if you accidentally something that should remain secret, like a password or an API key.
date_created: 2013-06-26
---

Although I always take the right measures to keep my database passwords to myself, I'll sometimes accidentally push a settings file with a little bit too much information and only notice a few commits later. Fortunately, I always notice before other people start pulling my work from the public repo.

In this tutorial, I will show you how to erase embarrassing things from your commit history without deleting the files in which they are. This implies you will overwrite history and force your next push, so use this technique sparingly.

First, find the commit you need. In this case, we leaked our database password in commit `bbc643cd`. Let's rebase to the commit right before we made our mistake (note the `^` at the end, it means *before*).

```
git rebase --interactive bbc643cd^

```

In the editor that will open, find your commit (`bbc643cd` in this example) and replace 'pick' with 'edit' on that line. Save the file. You can now make changes to that commit, and add them with `git add` as usual.

Once you've taken care of your mistakes, amend your changes to the commit we're editing

```
git commit --amend

```

then use the following command to return to the previous head commit:

```
git rebase --continue

```

If you try to push your changes, your remote server will probably protest since you are rewriting history. In our case, we DO want to rewrite history. We don't want any traces of our mistakes left in any commit. Therefore, we force the push:

```
git push -f

```

This is absolutely not something you want to do often, especially not if you're not alone to use that repository. However, mistakes happen, and it's better to anger a few people now than to deal with a security breach later.

