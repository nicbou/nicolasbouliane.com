---
title: Adding days to a Javascript Date object
description: How to add a few days to an existing Date object in JavaScript.
date_created: 2013-04-07
---

Adding an arbitrary amount of days is easy with Javascript. Using the `setDays()` method, it's pretty self-explanatory:

```javascript
//Adds a day to today 
var today = new Date();
var tomorrow = new Date();
tomorrow.setDate(today.getDate()+1); //Tomorrow = today + 1 day
```

