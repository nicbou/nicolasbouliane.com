---
title: How to fix "The Plugin Store is not available" in Craft
description: The surprisingly simple solution to this issue, and other cURL SSL errors. You only need to run a single command.
date_created: 2019-05-26
---

If you get the following error message when accessing the plugin store in Craft 3, this might be the solution.

```
The Plugin Store is not available
```

Open the Chrome Developer Tools console and reload the page. In the network tab, the request to the plugin store should return an HTTP 500 error. If you look at the content of the response, it should show a more detailed error. You can also find that error message in the Craft logs.

Here is the error I had:

```
cURL error 77: error setting certificate verify locations
```

If you got that error message, it's likely because cURL cannot find the right SSL certificates. This might be because you have moved or overwritten the `/etc/ssl` directory. You can usually fix this by running `update-ca-certificates`. This solution is not specific to Craft. It should fix this problem if it happens elsewhere.

This is all I needed to do. I would not have had that problem if I didn't overwrite `/etc/ssl`.

