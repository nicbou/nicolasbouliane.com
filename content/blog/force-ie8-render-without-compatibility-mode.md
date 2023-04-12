---
title: How to force IE8 to render without compatibility mode
description: If you still use IE8, something is deeply wrong. Godspeed, you poor soul.
date_created: 2014-02-13
---

Some companies force Internet Explorer 8 to render all pages using the Internet Explorer 7. This is what Microsoft calls "compatibility mode". Fortunately, you can override that setting and force IE to render the page using the latest version of its rendering engine (IE8+) with a simple meta tag.

Place this **before all other tags** in your `<head>`:

```html
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
```

In this example, we have added `chrome=1` to force the use of Chrome Frame if it's available on the client's computer.

You can also set this using an HTTP header, although the meta tag will take precedence over the header.

Please note that the browser will still pass as its older version, making browser detection useless. However, at the very least, it will render the page using the most recent rendering engine available.

Fortunately, with older versions of Internet Explorer quickly losing market share, this should not be necessary for very long.

