---
title: How to redo a South migration after using --fake
description: 
date_created: 2013-07-29
---

If you are using Django South, you might accidentally use `manage.py migrate [app] --fake` at some point. To undo your mistake, use the following commands:

```
python manage.py shell
from south.models import MigrationHistory
m = MigrationHistory.objects.get(migration="<migration_name>")
m.delete()
```

That's it! You can now safely perform your migration again.

