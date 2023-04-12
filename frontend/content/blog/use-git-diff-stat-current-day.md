---
title: How to see how many lines of codes were changed in a day with git
description: 
date_created: 2014-02-24
---

If you want to know how many files and how many lines of code were changed for the day, simply run the following command:

```
git diff --stat "@{1 day ago}" 
```

This will output a list of all changed files along with the number of lines added and removed, as well as a total for all files combined.

Naturally, you can also use different time intervals:

```
git diff --stat "@{2 weeks ago}" 
```

Although measuring productivity by counting lines of code is a rather ludicrous idea, it can give you an idea of how much has changed in a given period of time

