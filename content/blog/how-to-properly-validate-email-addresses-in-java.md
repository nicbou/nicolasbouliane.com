---
title: How to properly validate email addresses in Java
description: Java comes with the InternetAddress. It validates email addresses for you, so there's no need to write your own class.
date_created: 2013-04-04
---

If you are using Java, the `InternetAddress` class will validate your emails against the RFC 822 standard. The function below will filter out most invalid emails quickly:

```
public static boolean isValidEmailAddress(String email) {
 try {
 new InternetAddress(email).validate();
 } catch (AddressException ex) {
 return false;
 }
 return true;
}

```

This regex will also match email adresses. However, it's not bulletproof. Emails such as `n@n.n` or `____@--...` would still pass validation.

```
/^([a-z0-9_\.\+-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
```

