---
title: How to isolate the date from a Date object in Javascript
description: How to remove the hours, minutes and seconds from a Date object, and get just the date part.
date_created: 2013-04-07
---

Sometimes, you will need only the date part from a `Date` object. In order to truncate the time from the date, here is what to do:

```
//Create the date object
myDate = new Date(); //Current date and time
myDate.setHours(0,0,0,0); //Current date at midnight

```

If you deal with time a lot, you might want to use [moment.js](https://momentjs.com/).

