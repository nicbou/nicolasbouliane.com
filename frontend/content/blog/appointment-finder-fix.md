---
title: Bringing the Bürgeramt appointment finder back online
description: My tool went offline for a few months. A post-mortem of what happened.
date_created: 2024-06-07
categories:
    technology
---

Some time ago, I built a [Bürgeramt appointment finder](/projects/appointment-finder). It helps people get an appointment to register their address at the Bürgeramt. The tool is exceptional in two ways: it's available to everyone for free, and it follows the rules. I worked with the city for many months to get it sanctioned.

A month ago, the city started blocking requests from my bot, so it stopped working. I reached out to them, but got no answer. Days passed, and I started thinking that I would have to shut it down for good.

Then a kind city government employee told me what happened.

A while ago, my bot got banned because other people used [the same code](https://github.com/All-About-Berlin/burgeramt-appointments), but modified it to poll Berlin.de faster. This caused a flood of requests that appeared to come from my bot, and it got us all blocked. However, each instance has [a unique identifier](https://github.com/All-About-Berlin/burgeramt-appointments/blob/main/appointments/appointments.py#L41) in its user agent to distinguish them. I pointed this out, they adjusted the filter (I think), and my bot came back online.

This time, it was different. It's my host - DigitalOcean - that got blocked. Other people have been hosting unruly appointment bots on DigitalOcean. When their IP got blocked, they spun up another server to evade the ban. DigitalOcean's API made that very easy. Berlin just blocked DigitalOcean's whole IP range, so All About Berlin's IP got blocked too.

Once I knew this, the fix was simple. I moved the bot to a different server, and it started working again.

## Acknowledgements

I am very thankful to Mathias and the IKT-ZMS team for their help. The tool could not exist without them. Although they can't make exceptions for my bot, they've been kind enough to help me troubleshoot problems and keep it online.

Many on social media have suspected that the city government is working against me out of spite. This could not be further from the truth. From my perspective, they have repeatedly volunteered to help me, a random guy building tools for fun. I am very grateful for their help.