---
title: How to install Festival text-to-speech on Ubuntu
description: 
date_created: 2013-12-23
---

There is a very limited set of quality text-to-speech software for Linux. One of the commonly recommended solutions is Festival. As is common with open source software, you will need to Google your way through a bunch of old mailing list archives before you find the correct instructions to install it on your system.

Since I have spend a good deal of my time getting Festival to work properly on my rather ordinary Linux Mint setup, here are instructions to install it.

If you only use `sudo apt-get install festival`, you will get the following error:

```
WARNING
No default voice found in ("/usr/share/festival/voices/")
either no voices unpacked or voice-path is wrong
Scheme interpreter will work, but there is no voice to speak with.
WARNING

-=-=-=-=-=- EST Error -=-=-=-=-=-
{FND} Feature Token_Method not defined

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

This is because the `festival` package does not include something as trivial as a default voice. This means you need to install the default voice Festival looks for separately, as it is found in the `festvox-kallpc16k package`:

```bash
sudo apt-get install festival festvox-kallpc16k
```

Voilà! You should now be able to use Festival properly.

