---
title: How to fix "Cannot read property 'failedExpectations' of undefined"
description: While running Karma unit tests, you might run into the following error. Here's how it's fixed.
date_created: 2016-03-11
---

While running Karma unit tests, you might run into the following error: `Uncaught TypeError: Cannot read property 'failedExpectations' of undefined`. The cryptic error message might be a pain in the butt to debug, so let me save you some time.

In your tests, look for reassignment of the `result` variable. You are probably overwriting a variable from Karma, and this is what breaks your tests. In my case, I was assigning `this.result` in `beforeEach`, and renaming it to `this.promiseResult` fixed the error.

