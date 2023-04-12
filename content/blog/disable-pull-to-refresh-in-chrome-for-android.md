---
title: Disable "pull to refresh" in Chrome for Android
description: In mobile Chrome, pulling the top of the page will reload it. Although it's a convenient UI pattern, it might get in the way. Here's how it can be disabled.
date_created: 2015-08-07
---

In mobile Chrome, pulling the top of the page will reload it. Although it's a convenient UI pattern, it might get in the way if you are trying to implement gestures in your app.

After careful observation, I have come up with a simple solution.

## AngularJS

I have successfully disabled "pull to reload" with this AngularJS directive:

```
//Prevents "pull to reload" behaviour in Chrome. Assign to child scrollable elements.
angular.module('hereApp.directive').directive('noPullToReload', function() {
 'use strict';

 return {
 link: function(scope, element) {
 var initialY = null,
 previousY = null,
 bindScrollEvent = function(e){
 previousY = initialY = e.touches[0].clientY;

 // Pull to reload won't be activated if the element is not initially at scrollTop === 0
 if(element[0].scrollTop <= 0){
 element.on("touchmove", blockScroll);
 }
 },
 blockScroll = function(e){
 if(previousY && previousY < e.touches[0].clientY){ //Scrolling up
 e.preventDefault();
 }
 else if(initialY >= e.touches[0].clientY){ //Scrolling down
 //As soon as you scroll down, there is no risk of pulling to reload
 element.off("touchmove", blockScroll);
 }
 previousY = e.touches[0].clientY;
 },
 unbindScrollEvent = function(e){
 element.off("touchmove", blockScroll);
 };
 element.on("touchstart", bindScrollEvent);
 element.on("touchend", unbindScrollEvent);
 }
 };
});
```

It's safe to stop watching as soon as the user scrolls down, as the pull to refresh has no chance of being triggered.

Likewise, if `scrolltop > 0`, the event won't be triggered. In my implementation, I bind the touchmove event on touchstart, only if `scrollTop <= 0`. I unbind it as soon as the user scrolls down (`initialY >= e.touches[0].clientY`). If the user scrolls up (`previousY < e.touches[0].clientY`), then I call `preventDefault()`.

This saves us from watching scroll events needlessly, yet blocks overscrolling, and thus pulling to reload.

## jQuery

If you are using jQuery, this is the **untested** equivalent. `element` is a jQuery element:

```
var initialY = null,
 previousY = null,
 bindScrollEvent = function(e){
 previousY = initialY = e.touches[0].clientY;

 // Pull to reload won't be activated if the element is not initially at scrollTop === 0
 if(element[0].scrollTop <= 0){
 element.on("touchmove", blockScroll);
 }
 },
 blockScroll = function(e){
 if(previousY && previousY < e.touches[0].clientY){ //Scrolling up
 e.preventDefault();
 }
 else if(initialY >= e.touches[0].clientY){ //Scrolling down
 //As soon as you scroll down, there is no risk of pulling to reload
 element.off("touchmove");
 }
 previousY = e.touches[0].clientY;
 },
 unbindScrollEvent = function(e){
 element.off("touchmove");
 };
element.on("touchstart", bindScrollEvent);
element.on("touchend", unbindScrollEvent);
```

Naturally, the same can also be achieved with pure JS.

