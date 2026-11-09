---
title: Telling if a field is required in Django templates
description: If you want to tell whether a field in a template is required, use form.myfield.field.required as in the example below.
date_created: 2014-08-13
---

If you want to tell whether a field in a template is required, use `form.myfield.field.required` as in the example below:

{% raw %}```twig
{% for field in form %}
    <label for="{{ field.id_for_label }}">
        {{ field.label }}
        {% if field.field.required %}*{% endif %}
    </label>
    {{ field }}
    {{ field.errors }}
{% endfor %}
```{% endraw %}

In this example, there will be an asterisk next to the required fields.
