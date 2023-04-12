---
title: Pagination with Django's generic ListView
description: 
date_created: 2015-01-19
---

Did you know the Django ListView supports pagination out of the box? All you need to do is specify the number of items per page with the `paginate_by` attribute:

```
class ArticleList(ListView):
 model = Article
 paginate_by = 10
```

The queryset available in object_list will be paginated, so you will only get 10 results. `page_obj` and `paginator` will be added to the context so you can have pagination buttons and know which page you are on.

The documentation for this is buried under [MultipleObjectMixin's documentation](https://docs.djangoproject.com/en/1.7/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin).

