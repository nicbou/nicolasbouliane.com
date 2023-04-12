---
title: How to clone model instances in Django
description: 
date_created: 2013-07-24
---

Let's say you want to create an exact copy of your an object instance. All you need to do is set the primary key to None and save the object again.

```
object_copy = MyObject.objects.get(pk=...)
object_copy.pk = None
object_copy.save()

```

Tada! You now have a copy of your object with a new primary key.

