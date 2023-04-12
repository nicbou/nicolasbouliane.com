---
title: LocalStorage gotchas in Internet Explorer and Safari
description: A few localStorage issues with IE and Safari, and the workarounds for each of them.
date_created: 2016-05-06
---

`localStorage.setItem` will throw an "Access denied" error in Internet Explorer InPrivate Browsing mode. Likewise, Safari will give you `QUOTA_EXCEEDED_ERR: DOM Exception 22: An attempt was made to add something to storage that exceeded the quota.`

To avoid those errors, you will need to wrap your localStorage access in a try/catch block.

