---
title: Different PNG image colours in IE and Safari
description: If your PNG images look different in Internet Explorer and Safari, you're probably using the wrong colour space.
date_created: 2010-06-21
---

When displaying PNG pictures in Internet Explorer or Safari, there is a colour distortion with the images. If this will not cause any trouble with isolated pictures, it can ruin your design if you rely on superimposed images with the same background colour.

## Why it happening?

The gamma correction data included in a PNG image is used by browsers to make sure the image looks good when it's displayed on your screen. However, this so-called "correction" is not applied equally to all colors and images and thus two superimposed images can look different even if they use the same colors, effectively breaking the design in some browsers.

The full explanation can be found [here](http://hsivonen.iki.fi/png-gamma/).

## How do I fix this?

The fix to this is to simply not include gamma correction data with the images when you save them.

**In Photoshop CS4**, when you Save For Web & Devices, uncheck the *Convert to sRVB* box before you save your image.

You can also achieve this with **PNGCrush** and **TweakPNG**.

