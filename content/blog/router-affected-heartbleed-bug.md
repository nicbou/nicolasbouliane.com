---
title: Is my router affected by the Heartbleed Bug?
description: 
date_created: 2014-04-10
---

A few days ago, a catastrophic security vulnerability with OpenSSL dubbed the "heartbleed bug" was disclosed by a Google employee. I will not go in the details since [this article offers a fantastic explanation](http://www.troyhunt.com/2014/04/everything-you-need-to-know-about.html), but let's just say it's quite a big deal, and a lot of applications are affected.

Most sites have already started applying fixes and notifying their users, but aside from various websites, there are a few other devices that are affected, including routers.

If you are using **DD-WRT** build versions 19163 to 23882, then you are at risk and should update your router firmware immediately.

**OpenWRT** users are also affected according to various user reports. As for **Tomato** users, you are safe as long as you are using an official release, as pointed out by a reader in the comments.

If you have another router model, make sure it's not using OpenSSL between versions 1.0.1 (excluding 1.0.1g) and 1.0.2. If your firmware uses OpenSSL and was built between 2012 and april 2014, it's likely to be affected.

Was your router affected by the Heartbleed bug? Report your findings in the comments.

