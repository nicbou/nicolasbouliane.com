---
title: Why I disabled comments on my websites
description: In early 2020, I disabled comments on every website I run. Here is how and why I did it.
date_created: 2020-04-27
---

In early 2020, I disabled comments on every website I run. Here is how and why I did it.

## Most comments are bad

On [All About Berlin](https://allaboutberlin.com), readers shared their experience with Berlin's notoriously unpredictable bureaucracy. On Wiser Coder, they confirmed that 5 year old solutions still worked, or provided better ones. Some readers asked tricky questions that highlighted flaws in my content. These comments were invaluable, but they were a small minority.

![](/images/Bildschirmfoto-2020-04-27-um-11.00.26.png)

Other readers thanked me for my work. That felt really nice to hear, but it was not really useful to other readers, so I deleted them.

![](/images/Bildschirmfoto-2020-04-27-um-11.01.07.png)

Then there were the bad comments. Some were stupid, and others were downright nasty. I've been called a crook and even threatened with legal action.

![](/images/Bildschirmfoto-2020-04-27-um-11.23.59.png)

The bulk of the comments were simply spam. Spam filters handle some of them, but enough got through to make manual moderation a necessity. Auto-approving comments is just calling for trouble.

![](/images/Bildschirmfoto-2020-04-27-um-11.05.24.png)

Put simply, comments were not an exciting novelty, they were just work. Comment moderation was yet another thing I had to take care of every few days.

## Comments are hard

If you care at all about performance or privacy, comments can be hard to implement properly. On a simple website, they can easily become the most complex part of the frontend.

First, there's performance. Comments require a bunch of extra database queries, and make cache busting more difficult. On All About Berlin, disabling comments reduced my page load time from 900ms to 300ms, and greatly simplified caching. Now, most of All About Berlin is static, so I can cache everything without much thinking.

Second, there's privacy. If you want to outsource the job, you can use a third-party solution like Disqus or Facebook Comments. Those platforms are cleverly disguised ad networks, and I would rather avoid them. I do not feel comfortable loading those party scripts on my websites, or forcing users to sign in before they can comment.

I was happy with WordPress' commenting system and Akismet's excellent spam filter, but Craft CMS does not offer equivalent solutions. Verbb's [Comments](https://plugins.craftcms.com/comments) plugin ($50) did a reasonably good job, but the documentation was lacking, and the keyword-based spam filter wasn't enough.

## I just want to build websites, man!

None of these challenges are insurmountable, but they are still a barrier to putting content on the internet.

I build websites because it's fun, and it should remain fun. Comments are a chore to implement, and a chore to moderate. They are not [calm technology](https://calmtech.com/), and [they do not bring joy](https://en.wikipedia.org/wiki/Marie_Kondo#KonMari_method), so they got axed. Running a website in Germany is [burdensome enough](https://allaboutberlin.com/guides/website-compliance-germany) as it is.

## Email works better

My personal website does fine without comments, but All About Berlin depends on them. At the end of every page, I added a paragraph that invites readers to email me.

Emails trickle in at about the same rate as comments before them, but spam comments are completely gone. Reader questions and feedback are delivered straight to my inbox. I can triage, file and search those emails just like any other.

The emails I get tend to be more personal, more conversational. Each message is addressed to one person, not to an audience. It's signed with a name and a return address. It behoves one to be more considerate in their choice of words.

It has been a few years since I have made this decision, and I am still happy with it. In some cases, I have created widgets to let users provide very specific feedback about things like [wait times at the immigration office](/projects/immigration-office-wait-times). The data is automatically collected and aggregated, instead of polluting my mailbox. I pay attention to it when I choose to, and that's very valuable to me.