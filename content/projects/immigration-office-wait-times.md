---
title: Immigration office wait times
description: A tool that collects and displays feedback about the Landesamt für Einwanderung.
date_created: 2024-11-27
project_url: https://allaboutberlin.com/guides/auslanderbehorde-wait-times
categories:
    golden
    allaboutberlin
---

I have made [a tool](https://allaboutberlin.com/guides/auslanderbehorde-wait-times) to measure and display wait times at the Berlin immigration office. It collects user reports and shows statistics by department and residence permit type. It's on [All About Berlin](/projects/all-about-berlin) since November 2024, and it has collected hundreds of data points.

![Tool that shows LEA wait times](/images/lea-wait-times.png)

In September 2025, I have made another tool to measure [citizenship wait times](https://allaboutberlin.com/guides/citizenship-wait-times).

{% include "blocks/_tableOfContents.html" %}

## What's wrong?

For many, moving to Berlin means applying for a residence permit and renewing it every 2 to 4 years.

No one knows exactly how long this process takes. The immigration office does not measure that.[^1] Wait times vary from 1 to 10 months, depending on the department, the residence permit type, and pure luck.

While they wait, people are often left unable to start a new job and earn a living. Immigrants lose their job before they even start because of to those delays. A friend I was hosting ran out of savings before he even got a response from the immigration office. He had to move back to his home country. These are not isolated cases.

In other cases, their old residence permit expires, and they are unable to travel for months on end. They miss weddings and funerals, because they wouldn't be allowed back into Germany.

I navigate people through this process since 2017, and I still didn't have a precise idea of how long it takes. This needed to change.

By giving people a clear timeline of their residence permit application, their journey becomes more predictable, and much less stressful. It does not speed up the process, but it helps people plan around it. 

So I have built [a tool](https://allaboutberlin.com/guides/auslanderbehorde-wait-times) that collects reports from readers and measures wait times by department and residence permit type. There is [a separate page](https://allaboutberlin.com/guides/citizenship-wait-times) to measure citizenship wait times.

## Why I built this

I already wrote about [how predictability reduces anxiety](/projects/all-about-berlin), and how [a good map improves any journey](/blog/maps).

What makes ride sharing and food delivery apps so great in my mind is that they give you an ETA. You know when your driver is coming, so you can sit inside and finish your drink instead of waiting outside in the cold. The experience of waiting is greatly improved by knowing how long you are going to wait.

![Map showing a driver's ETA](/images/illustrations/map-eta.png)

Even when wait times are not known, you can hint at wait times. For example, Google Maps tells you how busy a restaurant is before you even get there.

![Google Maps showing how busy a place is](/images/illustrations/google-maps-busy-times.png)

I wanted to bring the same sort of predictability to a place where much more is at stake: the immigration office. It's one thing not to know when your lunch is coming, and another not to know when you will receive a regular paycheck and stop burning through your savings.

Other people also have a stake in this: your dependents who came to Germany with you, and your employer who is hoping you can start working soon. People regularly lose their job because they even start due to immigration office delays.

## How it works

Users fill a simple form to provide feedback about their journey. This form is placed in various guides in order to catch readers at the right time.

![Wait time feedback form](/images/blue-card-feedback.png)

The form is simple and highlights its social purpose.

![Detailed feedback collection](/images/blue-card-feedback-2.png)

People can provide partial feedback if they are not through with their journey. They can attach notes and useful advice to their report. Feedback is segmented by department and residence permit types.

![Email collection](/images/blue-card-feedback-email.png)

If they provide incomplete feedback, they can leave their email address. They will get reminders to complete their feedback in 2 and 6 months. Their email address is scrubbed from the database once the second reminder is sent.

If they scroll down, they can see feedback from individual users, along with comments.

![LEA wait times - Individual user reports](/images/lea-wait-time-feedback.png)

## How it's built

As other tools on All About Berlin, it's a simple Vue JS widget talking to a REST API. The backend used to be a bare bones Flask API, but I moved the entire thing to Django for this project. Switching to a familiar, batteries-included framework was a great decision.

[^1]: [Frag den Staat](https://fragdenstaat.de/anfrage/durchschnittliche-bearbeitungszeiten/) (June 2024)