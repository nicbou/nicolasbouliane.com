---
title: How to create a Date object for a specific date in Java
description: A simple tutorial on creating a date in Java.
date_created: 2013-04-04
---

Creating a new date in Java is quite simple. Use the [`Calendar`](http://docs.oracle.com/javase/1.5.0/docs/api/java/util/Calendar.html) class to quickly create your `Date` object

```
//Generate a date for Jan. 9, 2013, 10:11:12 AM
Calendar cal = Calendar.getInstance();
cal.set(2013, Calendar.JANUARY, 9); //Year, month and day of month
Date date = cal.getTime();

```

If you also need to set the time, you can use the `.set()` method with the following parameters:

```
//Generate a date for Jan. 9, 2013, 10:11:12 AM
Calendar cal = Calendar.getInstance();
cal.set(2013, Calendar.JANUARY, 9, 10, 11, 12); //Year, month, day of month, hours, minutes and seconds
Date date = cal.getTime();

```

Voilà! It's that simple! If you are still getting to grips with the Java programming languages, I recommend [Head First Java](http://amzn.to/2fUTYBV). It's a nicely paced introduction to Java.

