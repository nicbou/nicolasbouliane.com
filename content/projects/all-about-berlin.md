---
title: All About Berlin
description: A website that helps people settle in Berlin and navigate German bureaucracy. Gets over 50 000 visitors a month. Built with Craft.
date_created: 2017-09-20
project_url: https://allaboutberlin.com
repo_url: 
featured_image: images/aab-homepage.png
---

Moving to Germany is an ordeal. After surviving the worst of German bureaucracy, I tried to help others through it. I was an active helper in a few expat Facebook groups. Then I got tired of answering the same questions again and again. Instead, I put the answers on a website, and linked to that. I could write longer, better answers and keep them updated.

This website grew to over 150 000 page views per month, making it my most successful project by far. If someone moved here in the last 2-3 years, there's a good chance they've used the website for one thing or another. Some HR departments use it to onboard new employees from abroad.

Since 2020, I live from that website.

Here are some of my most popular guides:

- [How to move to Berlin](https://allaboutberlin.com/guides/moving-to-berlin)
- [How to register your address in Berlin](https://allaboutberlin.com/guides/anmeldung-in-english-berlin)
- [How to apply for the German freelance visa](https://allaboutberlin.com/guides/how-to-get-a-german-freelance-visa)
- [How to choose German health insurance](https://allaboutberlin.com/guides/german-health-insurance)

## They don't make 'em like that anymore

This website is my answer to the hastily written SEO spam that dominates the search results. It's free, straightforward and useful. I wanted to prove that you could build and monetise a website without annoying the everliving crap out of my readers.

It has no ads, no paywalls, no newsletter popup, no coercive cookie notice, no calls to action, no comments, no promoted content, and no share buttons. It gives you straight, honest answers. That's it.

All About Berlin is supported by affiliate links, which bring its own ethical challenges. It's tempting to put monetisation first, but I manage just fine without blurring the line between advice and advertising. I frequently remind advertisers of my [content policy](https://allaboutberlin.com/contact#content-policy).

## Information, tools, policy

The website follows a three tier strategy: information, tools, policy.

Information is about providing helpful, neutral advice to readers. I try to represent a complex bureaucratic system with simple, well-structured guides.

Tools give *personalised* information. My [health insurance calculator](https://allaboutberlin.com/tools/health-insurance-calculator) and [income tax calculator](https://allaboutberlin.com/tools/tax-calculator) replace lots of tedious reading with a few simple questions. Tools also mean referring people to the right experts when they get stuck.

Policy is a much tougher nut to crack. It's about fixing the root cause, instead of dancing around it. I have made a few attempts to work directly with the city of Berlin, and enjoyed some limited success.

## Delivered in 500 milliseconds or less

All About Berlin is ludicrously fast, and that's no accident. I spent quite a bit of time shaving milliseconds off the page load time.

I use aggressive [static caching](https://craftcms.stackexchange.com/questions/21171/static-page-caching-using-nginx-fastcgi-cache-with-craftcms) to reduce the [time to first byte](https://en.wikipedia.org/wiki/Time_to_first_byte) to around 20 milliseconds. I use [HTTP2 server push](https://www.smashingmagazine.com/2017/04/guide-http2-server-push/) to serve all the assets in a single request. I inline the minimalist CSS and JS to save server round trips. I serve fonts locally and reverse-proxy Plausible's tracking script to avoid additional DNS requests. I use [lazyloaded](https://web.dev/native-lazy-loading/), [responsive](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images) images to send as few bytes as possible across the wire. And of course, the pages themselves are just text on a page, so they're quite small.

All of these optimisations let me run a really fast website on really cheap hardware.

## Keeping it all up to date

The biggest challenge with such a website is to keep its information up to date. There are over 100 guides that require constant updates. I have a few tricks up my sleeve to make my work easier.

I use [Wachete](https://www.wachete.com/) to monitor certain pages. If they change, I get an email notification. This is how I keep track of changes in the address registration and visa application processes. Wachete costs 5€ a month, and it's a life saver.

I use global variables for various numbers on the website. If the maximum health insurance contribution changes (as it does every year), I update one variable, and the changes spread to the entire website.

I can update information in one place, but forget to update it in another. This is why I [don't repeat myself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), and try to [keep the information in a single place](https://en.wikipedia.org/wiki/Single_source_of_truth). Guides frequently link to each other, just like Wikipedia articles do.

![](/images/Screenshot-2021-11-18-at-09.19.54.png "Guides link to each other to avoid repetition")

I use a glossary for the same reason. It keeps the information in one place, and it keeps readers informed without wasting space.

![](/images/all-about-berlin-glossary.png "The glossary explains terms without wasting space")

## Clever bits

To give better explanations, I have built [tools and calculators](https://allaboutberlin.com/tools) that I embed in the content. I also implemented a [currency conversion tooltip](/blog/currency-tooltips) for newcomers to the Eurozone. It's a good way to apply my programming skills after leaving my software development career, and it's often a more efficient way to explain things to readers.

![](/images/currency-conversion-tooltip.png "The currency conversion tooltip translates euro amounts to a familiar currency.")

## Built with Craft

All About Berlin is a [Craft CMS](https://craftcms.com/) website that runs inside docker on a [Digital Ocean](https://www.digitalocean.com/) VPS. The theme is 100% custom-made. I much prefer Craft to Wordpress. It has a much more flexible data structure that lets me build the website exactly as I want it.

![Aab homepage](/images/aab-homepage.png)

![Aab guides](/images/aab-guides.png)

![Aab guide 2](/images/aab-guide-2.png)

![Aab guide 1](/images/aab-guide-1.png)

