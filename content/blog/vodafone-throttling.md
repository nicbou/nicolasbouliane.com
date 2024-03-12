---
title: Vodafone Germany is throttling upload speed
description: It's not just you. You don't get the upload speed that you pay for.
date_created: 2024-03-12
---

I am travelling in Asia. When I try to download large files from my [home server](/projects/home-server) in Germany, Vodafone throttles the speed to 60-150 kbps. Files that should take a few minutes to download take 2-3 hours.

Through a process of elimination, I confirmed that **Vodafone is throttling my connection**, but seemingly only when I download from a Malaysian connection. I reproduced this from a dozen locations in Singapore and Malaysia.

If I use a VPN or an SSH tunnel based in Germany, there is no throttling. Files download at the normal speed.

I asked my friends to download the same file (from Germany) and there was no throttling.