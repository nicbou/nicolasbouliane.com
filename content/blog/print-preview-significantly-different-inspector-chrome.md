---
title: Print preview significantly different from Inspector in Chrome?
description: Are you having issues with the Chrome print media emulator showing different results from print preview? Here's how I solved this problem.
date_created: 2014-05-07
---

Are you having issues with the Chrome print media emulator showing different results from print preview? Here's how I solved this problem.

In the emulator, my styles were showing just fine, but despite all the `!important` rules in the world, nothing would work in print preview. It turns out the print preview will display your page before CSS transitions are applied, so if there's a transition when some elements are moved, print preview will show them *before* that transition. This is especially tricky if you use CSS transitions for columns, responsive design, slide out menus etc.

Adding `*{transition:none!important}` in the print stylesheet fixed it for me.

