---
title: Tastypie: only allow a user to use its own resources
description: 
date_created: 2013-11-05
---

If you want to limit user access to the resources they own in Tastypie, define `obj_create` and `apply_authorization_limits` as such. This will automatically assign created items to the current user, and only return resources that belong to the current user.

```python
from tastypie.resources import ModelResource
from notes.models import Note


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'

    # ...

    def obj_create(self, bundle, **kwargs):
        """
        Assign created notes to the current user
        """
        return super(NoteResource, self).obj_create(bundle, user=bundle.request.user)

    def apply_authorization_limits(self, request, object_list):
        """
        Return the user's notes
        """
        return object_list.filter(user=request.user)
```

This example is taken straight from the official documentation

