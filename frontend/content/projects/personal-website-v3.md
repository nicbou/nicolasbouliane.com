---
title: Personal website 3.0
description: A simpler, faster, mobile-friendly rewrite of my personal website.
date_created: 2020-07-03
project_url: https://nicolasbouliane.com
repo_url: 
featured_image: images/ticks.png
---

Few projects of mine have been as uninspired as the redesign of my personal website.

The original plan was to tell the story of my a long motorcycle trip. The trip happened, but the blog didn't. I underestimated how much work it takes to document a trip while still enjoying it. Besides, a good story is better shared over a pint than over the net.

The project drifted for a year, until I buckled down and finished it, borrowing heavily from [All About Berlin](/projects/all-about-berlin)'s infrastructure.

## This time, it's personal

My old website was a professional portfolio. It was built to attract recruiters. Now, I live from [a website I built](/projects/all-about-berlin), and this flashy online presence lost its purpose. In its stead, I built a truly personal website on which I could share things I truly care about.

![](/images/old-nicolasbouliane-website.png "My old website's front page")

This change of priorities gave me more creative freedom. I [got rid of comments](/blog/no-comments-on-website) and ditched analytics because they don't matter to me. I added a [recipes](/recipes) section, achievements and a dark mode, because it was fun.

## Technical improvements

The old website ran on WordPress. It didn't support HTTPS. It wasn't even mobile-friendly, and on the big screen, the tiny font strained my eyes.

This rewrite features an extra decade of web development experience, including many lessons learned while running All About Berlin. It's simpler, faster, mobile-friendly, more secure and more readable.

 This time, I built it with [Craft](https://craftcms.com/), served it with nginx, and ran it inside docker. Craft makes the website easier to maintain and extend. Nginx makes it faster. Docker makes it easier to deploy. The entire infrastructure is under source control, so deploying the project to a new server takes a few minutes. The old site was a WordPress install running directly on the host.

## Garbage collection

With this redesign, I also wanted to remove a decade of old stuff. The server that hosted nicolasbouliane.com also hosted wisercoder.com, and a miscellany of other small projects. Those only stayed online because it was more trouble to remove them, or because I simply forgot about them.

![](/images/ticks.png "Ticks")

![](/images/axelipsum.png "Axel Ipsum")

![](/images/wisercoder.png "Wiser Coder")

![](/images/trlygd.png "Trly.gd")

![](/images/billsplitter.png "Bill Splitter")

I moved the content from wisercoder.com to my personal website, redirected all traffic to it, and let the domain expire. Everything else got deleted.

Now, there's just this website, and it's good enough.