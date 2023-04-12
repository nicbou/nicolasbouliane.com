---
title: OS X: Make a sound when commands finish running
description: How to get an audible notification after a command ends.
date_created: 2013-08-02
---

If you are like me, you might get distracted while waiting for your unit tests to complete, and only return to your IDE several minutes later.

On OS X, there is a nifty `say` command that makes your Mac say anything you want using text-to-speech. By appending it at the end of a long-running command, you can get a voice notification when it completes.

In the example below, your Mac will say "Unit tests completed" when they are done running:

```bash
python manage.py test; say "Unit tests completed"
```

