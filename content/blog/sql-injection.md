---
title: What is SQL injection?
description: 
date_created: 2014-03-28
---

SQL injection allows a hacker to inject malicious SQL statement by exploiting improperly sanitised queries. It is by far one of the most common attack vectors, and was used in [several famous exploits](http://en.wikipedia.org/wiki/SQL_injection#Examples).

For example, let's say we use user-submitted form data to check a user's credentials:

```
sqlQuery = "
 SELECT * FROM users
 WHERE username='" + username + "'
 AND password='" + password + "'
";
```

Normally, that query would only return a user with a matching user name and password, but if the hacker uses an existing username (e.g. `eric123`), but injects SQL in the password field (e.g. `' OR '1'='1`), then the query will be completely altered:

```sql
SELECT * FROM users
WHERE username='eric123'
AND password='' OR '1'='1'
```

This query would return the user's record and the application would log the user in even though no password was supplied. By using semicolons, a user could even insert entirely new queries:

```sql
SELECT * FROM users
WHERE username='eric123'
AND password=''; DELETE FROM USERS WHERE '1'='1'
```

In the scenario above, all the hacker had to do was to use `'; DELETE FROM USERS WHERE '1'='1` in the password field.

SQL injection can be prevented by using [query parameterization](https://www.owasp.org/index.php/Query_Parameterization_Cheat_Sheet).

