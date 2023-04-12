---
title: Common pocketsphinx mistakes and how to fix them
description: 
date_created: 2013-12-22
---

In the past few months, I have been using pocketsphinx as the speech recognition engine for a personal project. Unfortunately, pocketsphinx is one of the old school open source projects with lacking documentation, uncommented source code and very limited examples. If you are used to the new wave of heavily documented open source projects, you might have hit quite a few bugs that seemingly nobody solved.

I have hit those bugs too. Here are some of them and their fixes.

**"Acoustic model definition not specified"**

On a fresh pocketsphinx install, you might have hit that error while running `pocketsphinx_continuous`:

```
ERROR: "acmod.c", line 85: Acoustic model definition is not specified neither with -mdef option nor with -hmm
```

There is usually a default acoustic model that is specified, as hinted by a contributor [here](https://sourceforge.net/p/cmusphinx/discussion/help/thread/980263ec/). If your computer can't find it, it's probably because you are missing a package.

If you are using Ubuntu or one of its derivatives such as Linux Mint, make sure you have the `pocketsphinx-hmm-en-hub4wsj` package installed. That solved it for me.

**More to come**

I will be adding more common errors here as I stumble upon them. If you are stuck with an error you don't understand, put it in the comments just in case.

