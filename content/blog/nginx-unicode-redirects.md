---
title: Nginx redirects with unicode characters
description: This is how you configure nginx redirects for URLs with accented characters.
date_created: 2023-07-06
---

On [All About Berlin](https://allaboutberlin.com), some URLs have accented characters. Recently, I renamed `/glossary/Bundesagentur für Arbeit` to `/glossary/Agentur für Arbeit`. To make this redirect work in nginx, I had to add `(*UTF8)` in front of the regex pattern:[^2]

```
# Before
rewrite "^/glossary/Bundesagentur für Arbeit" "/glossary/Agentur für Arbeit" permanent;

# After
rewrite "(*UTF8)^/glossary/Bundesagentur für Arbeit" "/glossary/Agentur für Arbeit" permanent;
```

This also works with nginx maps, and with redirects that use the `return 301 /path/to/new-url;` format.[^1]

[^1]: [blog.rabin.io](https://blog.rabin.io/quick-tip/matching-non-ascii-characters-in-nginx-location)
[^2]: [Stack Overflow](https://stackoverflow.com/questions/28055909/does-nginx-support-raw-unicode-in-paths), [Server Fault](https://serverfault.com/questions/656096/rewriting-ascii-percent-encoded-locations-to-their-utf-8-encoded-equivalent)