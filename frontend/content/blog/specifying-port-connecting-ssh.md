---
title: Specifying a port when connecting with SSH
description: To connect to SSH on a port other than 22, use the -p flag.
date_created: 2014-07-21
---

Some servers run their SSH server on a different port than 22 for a variety of reasons, including security.

To specify a custom port when connecting, use the `-p` flag as in the example below:

```
ssh user@server.com -p 2222

```

In this example, the client would attempt to connect using port 2222.

