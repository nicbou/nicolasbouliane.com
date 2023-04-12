---
title: How to fix a beeping/buzzing hard drive
description: If you hard drive beeps or buzz, you might be able to fix it yourself. Here's how.
date_created: 2020-09-24
---

A few days ago, the hard drive on my ThinkPad T510 stopped booting. When I booted the laptop, I got the following error:

```
Error 2100 HDD0 initialization error (1)
```

If I went in the BIOS setting, the hard drive was not detected. I borrowed a friend's hard drive dock. When I put the hard drive in the dock, started making a [beeping noise](https://www.youtube.com/watch?v=7m5cil6KezI).

With nothing to lose, I opened the hard drive. There were 6 screws around the edge, and 1 hidden under the label. As soon as I removed the hard drive cover, I saw that **the head was stuck on the platter**. The noise came from the struggling head motor.

![](/images/seagate-harddrive-teardown.jpg)

![](/images/seagate-hard-drive-hidden-screw.jpg "There is a hidden screw under the label.")

![](/images/seagate-laptop-hard-drive-stuck-head.jpg "The head is stuck over the platter. It should be stowed on the side.")

I used my screwdriver to rotate the platter, and pushed the head back in place with my finger. I reassembled the hard drive, and the laptop booted right away. This let me <del>extract all the important data</del> use it as a primary drive for another 6 months before replacing it.

