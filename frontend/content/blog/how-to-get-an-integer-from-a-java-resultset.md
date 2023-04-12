---
title: How to get an Integer from a Java ResultSet
description: A simple tutorial on getting an integer from a ResultSet
date_created: 2013-04-04
---

By default, `ResultSet.getInt(...)` only returns an int. If the database value is null, it will return 0. This is already covered in the documentation: "The default for ResultSet.getInt when the field value is NULL is to return 0". This is also the case for `resultset.getFloat()`.

This irritating behavior can easily be fixed with the `wasNull` method:

```
Integer myInt = resultSet.getInt("nullable_column"); //Returns 0 even if the value should be null
if (resultSet.wasNull()) {
 myInt = null;
}
```

This way, your `resultSet.getInt(...)` will correctly set null values instead of returning 0.

