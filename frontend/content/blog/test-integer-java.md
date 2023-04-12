---
title: How to test for an integer in Java
description: 
date_created: 2013-12-06
---

Java doesn't have a tryParse method for integers. However, you can verify for an integer using the following method:

```
public static boolean isInteger(String s) {
 try { 
 Integer.parseInt(s); 
 } catch(NumberFormatException e) { 
 return false; 
 }
 // only got here if we didn't return false
 return true;
}
```

