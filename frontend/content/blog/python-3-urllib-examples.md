---
title: Python 3 urllib examples
description: How to do basic things with urllib in Python 3.
date_created: 2020-04-30
---

This article is the missing manual for Python 3's urllib. It shows you how to do basic things that are not clearly described in the official documentation.

The [requests](https://requests.readthedocs.io/en/master/) library is much easier to use than urllib. Only use urllib if you want to avoid external dependencies.

## Request a URL, read response content

To make an HTTP request download a page with urllib, you must call [urllib.request.urlopen()](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen).

```
import urllib.request

response = urllib.request.urlopen('https://nicolasbouliane.com')
response_content = response.read()

print(response_content)
# "<!doctype html>\n<html..."
```

A few notes:

- urlopen() returns a [http.client.HTTPResponse](https://docs.python.org/3/library/http.client.html#httpresponse-objects) object
- urlopen() automatically follows redirects
- urlopen() throws an [HTTPError](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError) on when the server returns an error response like HTTP 404 or 500.

## Get response status code

To make an HTTP request download a page with urllib, you must call [urllib.request.urlopen()](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen).

```
from urllib.error import HTTPError
import urllib.request

try:
 response = urllib.request.urlopen('https://nicolasbouliane.com')
 response_status = response.status # 200, 301, etc
except HTTPError as error:
 response_status = error.code # 404, 500, etc
```

A few notes:

- urlopen() automatically follows redirects. You will see the status code of the destination URL.
- urlopen() throws an[HTTPError](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError) on when the server returns an error response like HTTP 404 or 500.

## Get response headers

urllib.request.urlopen() returns a [http.client.HTTPResponse](https://docs.python.org/3/library/http.client.html#httpresponse-objects) object. You get headers by calling [response.getheaders()](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.getheaders) or [getheader(header_name)](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.getheader).

```
import urllib.request

response = urllib.request.urlopen('https://nicolasbouliane.com')
headers = response.getheaders()
content_type = response.getheader('Content-Type')

print(headers)
# [('Content-Type', 'text/html; charset=utf-8'), ('Transfer-Encoding', 'chunked'), ...]

print(content_type) 
# "text/html; charset=utf-8"
```

A few notes:

- getheader() is not case-sensitive. getheader('Date') and getheader('date') will return the same value.
- getheaders() returns a list of two-tuples, not a dict.

