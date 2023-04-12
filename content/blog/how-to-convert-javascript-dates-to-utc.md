---
title: How to convert dates to UTC in vanilla JavaScript
description: A simple tutorial on removing timezones from JavaScript dates.
date_created: 2013-04-14
---

When you create a JavaScript `Date` object, it will set the date in your time zone. If you want to keep the same date, but convert it to UTC/GMT for storage and comparison purposes, use the function below:

```
//Converts a Date object to its equivalent in UTC time.
function dateToUTC(date) {
 return new Date(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate(), date.getUTCHours(), date.getUTCMinutes(), date.getUTCSeconds());
}
```

This will convert a date such as `January 6, 17:24 EST` to `January 6, 17:24 GMT`.

