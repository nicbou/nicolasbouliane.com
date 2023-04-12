---
title: Add some color to the OSX Terminal
description: If you find the OS X Terminal's lack of color hard on the eyes, here's how to set the colors.
date_created: 2013-11-26
---

If you find the OS X Terminal's lack of color hard on the eyes, here's how to set the colours.

Open `~/.bash_profile` and add this:

```bash
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
export PS1="[\033[36m]\u[\033[m][\033[32m]:[\033[33;1m]\W[\033[m]\$ "
alias ls='ls -GFh'

```

The first line enables colours, the second sets the colors for `ls` and the last one sets the terminal's color scheme. Finally, the last line enables color by default on the `ls` command.

You will find a more detailed description of the colour scheme syntax [here](http://blog.taylormcgann.com/tag/prompt-color/).

