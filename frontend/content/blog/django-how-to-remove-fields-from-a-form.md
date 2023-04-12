---
title: Django: How to remove fields from a Form
description: 
date_created: 2013-07-05
---

Let's say you want to inherit from the following form:

```
class SuperLongForm(forms.Form):
 first_name = ...
 last_name = ...
 ...

```

And that you want to recreate the same form, but without the `last_name` field. All you have to do is to remove the field from the fields dict:

```
class FirstNameOnlyForm(SuperLongForm):
 def __init__(self, *args, **kwargs):
 super(FirstNameOnlyForm, self).__init__(*args, **kwargs)
 self.fields.pop('last_name')

```

Keep in mind that this is not the smartest way to do thing. Two forms inheriting from a base form with the `first_name` field would be a much smarter decision.

