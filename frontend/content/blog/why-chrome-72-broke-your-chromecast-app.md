---
title: Why Chrome 72 broke your Chromecast app
description: Chrome 72 made some changes to the Chromecast API. Here's why your Chromecast app suddenly stopped working.
date_created: 2019-02-19
---

Since Chrome 72 came out, the Chromecast button stopped working on my home server. Plex and Emby users report similar having issues. This change was not officially announced, but it happens on all platforms.

If your Chromecast sender application stopped working, it's probably because Chrome only supports casting from HTTPS sources since Chrome 72 (released in early 2019). If you serve cast_sender.js from an HTTP source, casting will not work. **The solution is to switch your website or Plex server to HTTPS.**

Related pages:

- [Mention of the issue for Plex](https://www.reddit.com/r/Chromecast/comments/ar6pro/problems_with_new_chrome_versions/)
- [Mention of the issue for Emby](https://emby.media/community/index.php?/topic/69363-chromecast-problem/)
- [Official deprecation report](https://www.chromestatus.com/feature/5766218384408576)

