---
title: Return a user's own objects with Django's class-based views
description: There is a very simple way to only return the connected user's own objects with Django's generic class-based views.
date_created: 2015-01-19
---

There is a very simple way to only return the connected user's own objects with Django's generic class-based views.

When you extend get_queryset() on any view that implements SingleObjectMixin or MultipleObjectMixin (almost all of them), you can filter the default QuerySet to match your needs. It becomes fairly easy to create a mixin that filters any queryset to return objects created by the current user.

This is the mixin we will be using:

```
class OwnObjectsMixin():
 """
 Only returns objects that belongs to the current user. Assumes the object
 has a 'user' foreignkey to a User.
 """
 def get_queryset(self):
 user = self.request.user
 return super(OwnObjectsMixin, self).get_queryset().filter(user=user)

```

Let's say you have a Bookmark model that has a foreign key called `user` that points to the standard User model. UserList view would look like this:

```
class UserList(OwnObjectsMixin, ListView):
 model = User

class UserDetails(OwnObjectsMixin, DetailView):
 model = User

```

You can use that mixin with CreateView, DeleteView and UpdateView too, making your views simple and maintainable.

