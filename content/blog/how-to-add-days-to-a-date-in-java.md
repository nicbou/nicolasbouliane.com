---
title: How to add days to a date in Java
description: A simple tutorial on adding time to a Date object in Java.
date_created: 2013-04-04
---

To add years, days, hours or minutes to a `Date` object in Java, you need to use the [`java.util.Calendar`](http://docs.oracle.com/javase/1.5.0/docs/api/java/util/Calendar.html) class.

```
//Adds one day to the current date
Calendar cal = Calendar.getInstance(); // The current date
cal.add(Calendar.DAY_OF_MONTH, 1);
Date date = cal.getTime(); // 1 day in the future
```

If you want to *substract* time, simply use a negative number.

```
//Five hours ago
Calendar cal = Calendar.getInstance();
cal.add(Calendar.HOUR, -5);
Date date = cal.getTime();
```

There's nothing more to it; it's that simple!

