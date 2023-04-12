---
title: How to fix slow file read/write in Node.js
description: It's probably your antivirus software
date_created: 2015-05-11
---

This morning, I had trouble with one of my grunt tasks taking several minutes to finish instead of 3-4 seconds. After a bit of troubleshooting, I isolated the bottleneck to a bunch of seemingly harmless file reads.

Guess who was the culprit? The company-supplied McAfee. Turning off on-access scan immediately fixed the issue and dropped the build time from 3 minutes to 5 seconds.

