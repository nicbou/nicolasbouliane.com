---
title: Fixing 'Can't use function return value in write context' in PHP
description: How to fix this error. At least how I fixed it back in 2014.
date_created: 2014-03-05
---

You might have encountered this error in one of your PHP scripts. Although the reason for this problem is a testament to how completely messed PHP is, it is quite simple.

Let's take a look at this function for example:

```javascript
if(empty(trim($var))){ //Can't use function return value in write context
 ...
```

The reason is that `empty()` is not a function but a language construct, and will only work on variables, not function return values.

This would work just fine:

```javascript
$var = trim($var);
if(empty($var)){ //All good
 ...
```

That's PHP for you.

