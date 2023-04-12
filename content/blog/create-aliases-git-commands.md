---
title: How to create aliases to git commands
description: 
date_created: 2013-11-26
---

You can set aliases for common git commands using the following command:

```
git config --global alias.poule pull
```

In this instance, we create an alias for `git pull` so `git poule` does a pull. Since we have used the `--global` flag, this applies to all of your projects.

Here is a more useful alias. It shows a short, colorful git log including the history graph. Call it with the `git lg` command.

```
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

You can find a list of your aliases and other config options in the `.gitconfig` file in your home directory.

