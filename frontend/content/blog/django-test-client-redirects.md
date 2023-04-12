---
title: Following redirects with the Django test client
description: When running unit tests with in Django, the test client's default behaviour is to stop at the first response, even if that response is a redirect.
date_created: 2014-06-11
---

When running unit tests with in Django, the test client's default behaviour is to stop at the first response, even if that response is a redirect.

If you want the client to follow these redirects and return the last page, perform your requests like this:

```
response = c.get('/redirect_me/', follow=True)

```

This will also add `response.redirect_chain` so you can see which URLs it followed before getting to the final page. Here is a sample redirect_chain:

```
[(u'http://testserver/next/', 302), (u'http://testserver/final/', 302)]
```

