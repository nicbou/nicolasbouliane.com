---
title: Ping once and return true/false
description: 
date_created: 2014-05-19
---

The `ping` command will usually try pinging a device forever, returning the response time after each pingback. If you want to ping a device once and use the answer to perform an action, use the following snippet:

```
ping -c 1 [your ip or hostname] > /dev/null
```

This command will either return 1 on failure or 0 on success.

In the example below, we use the `&&` operator to perform an action if and only if the ping to "homeserver" was successful:

```
ping -c 1 homeserver >/dev/null && echo 'Successfully pinged device!'
```

This can be a great way to monitor the presence of a device on the network for a dead man's switch for example.

