---
title: SQL Server: How to add a month to the current date
description: 
date_created: 2014-02-24
---

If you want to add a month to the current date in SQL Server, use the `DATEADD` function.

In this example, we add 1 month to the current date by combining it with `GETDATE()`:

```
DATEADD(mm,1,GETDATE())

```

In this second example, we add two months to a date from another column called `other_column`:

```
DATEADD(mm,2,other_column)

```

You can use `DATEADD` to add hours, days, weeks or years to a date. You can find more information about this function in the [documentation](http://technet.microsoft.com/en-us/library/ms186819.aspx).

