---
title: How to throttle scroll events in AngularJS
description: 
date_created: 2015-08-10
---

If you watch the scroll event, you will probably find yourself handling far more events than you need. The scroll event fires *really* quickly, and that can be a problem on mobile devices.

The following Angular directive will call a specified scroll event every 250 milliseconds.

```
angular.module('hereApp.directive').directive('onScroll', function($timeout) {
 'use strict';

 return {
 scope: {
 onScroll: '&onScroll',
 },
 link: function(scope, element) {
 var scrollDelay = 250,
 scrollThrottleTimeout,
 throttled = false,
 scrollHandler = function() {
 if (!throttled) {
 scope.onScroll();
 throttled = true;
 scrollThrottleTimeout = $timeout(function(){
 throttled = false;
 }, scrollDelay);
 }
 };

 element.on("scroll", scrollHandler);

 scope.$on('$destroy', function() {
 element.off('scroll', scrollHandler);
 });
 }
 };
});
```

The scrollable element should look like this:

```
<div on-scroll="myScrollEvent()"></div>
```

