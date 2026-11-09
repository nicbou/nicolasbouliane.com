---
title: The connection string to use with PHP, dblib and SQL Server
description: This is how you make PHP connect to SQL server.
date_created: 2014-03-26
---

If you are trying to connect to an SQL Server database with the dblib drivers for PDO, this is the correct connection string to use:

```php
new PDO('dblib:host='.$host.';dbname='.$database, $this->user, $this->password);
```

You can also specify the encoding with `charset=UTF-8` or `charset=ISO-8859-1` if necessary.

Be aware that dblib is incredibly buggy and that it does not support unicode or transactions. I have also encountered important other bugs, such as being unable to use `ERRMODE_EXCEPTION`. However, there are not that many alternatives if you want have to connect to SQL Server from PHP on Linux

