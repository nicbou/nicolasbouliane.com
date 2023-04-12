---
title: Django unit tests: How to populate request.raw_post_data
description: In the example below, we are testing how our view reacts to a raw POST string sent by another API.
date_created: 2013-06-17
---

If you are creating unit tests with Django, you might need to send raw data with the Client object. In the example below, we are testing how our view reacts to a raw POST string sent by another API. The string in question is `myrawpoststring`.

All you need to do is set the `data` attribute to your string, then set the content_type attribute to `application/octet-stream`. The default content type, `multipart/form-data`, expects a dictionary. Any other value will accept raw strings, including made-up content types. Semantically, the `application/octet-stream` content type is the correct one to use.

```python
class MyTestCase(TestCase):
    # ...

    def test_partial_refund(self):
        # Send a request to /api/sync/23/ with a raw POST string
        response = self.client.post('/api/sync/23/', data='myrawpoststring', content_type='application/octet-stream')
```

The `.put()`, `.patch()` and `.delete()` equivalents already set the content_type to 'application/octet-stream' by default, so you will only need to specify a string.

In your view, you will now be able to access your string in the request object:

```python
def my_simple_view(self, request):
    post = request.raw_post_data  # post will equal 'myrawpoststring'
    # ...
```

