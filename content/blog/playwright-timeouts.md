---
title: Fixing TimeoutErrors with Playwright on MacOS
description: Are you getting random TimeoutErrors with Playwright? It's probably because you switched desktops.
date_created: 2024-01-03
---

While running Playwright tests in Firefox (using Python and pytest), I kept getting random timeout errors. If I ran the same tests again, it would work fine. On the next run, a different set of tests would time out. The timeouts happened at different steps.

The reason? Multiple desktops. Playwright tests running on a different workspace time out. Playwright tests running in the background on the current workspace run just fine.