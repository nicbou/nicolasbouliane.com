---
title: Django DeleteView with AJAX
description: Djangos generic DeleteView is not really made for AJAX requests. A simple AjaxDeleteView can be implemented instead.
date_created: 2015-01-19
---

The default Django generic DeleteView is not perfectly adapted for AJAX requests. A much simpler AjaxDeleteView can easily be implemented using the same mixins as Django's generic class-based views:

```
class AjaxDeleteView(SingleObjectMixin, View):
 """
 Works like DeleteView, but without confirmation screens or a success_url.
 """
 def post(self, *args, **kwargs):
 self.object = self.get_object()
 self.object.delete()
 return HttpResponse(status=204)

```

This views performs CSRF validation just like the default DeleteView, except it won't show any confirmation screens and has no need for the success_url attribute.

