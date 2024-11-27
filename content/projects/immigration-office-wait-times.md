---
title: Immigration office wait times
description: A tool that collects and displays feedback about the Landesamt für Einwanderung.
date_created: 2024-11-30
project_url: https://allaboutberlin.com/guides/auslanderbehorde-wait-times
categories:
    golden
    allaboutberlin
---

I made [a tool](https://allaboutberlin.com/guides/auslanderbehorde-wait-times) that collects and displays feedback about wait times at the Berlin immigration office.

![Tool that shows LEA wait times](/images/lea-wait-times.png)

{% include "blocks/_tableOfContents.html" %}

## Introduction

For many, moving to Berlin means applying for a residence permit and renewing it every 2 to 4 years.

No one knows exactly how long this process takes. Wait times vary from 1 to 10 months, depending on the department, the residence permit type, and pure luck.

While they wait, people are often left unable to start a new job and earn a living. People frequently lose their job before they even start due to immigration office delays.

In other cases, their old residence permit expires, and they are unable to travel outside Germany for months on end. People miss weddings and funerals, unable to secure the *[Fiktionsbescheinigung](https://allaboutberlin.com/guides/fiktionsbescheinigung)* that would let them re-enter the country.

I navigate people through the immigration process since 7 years, and I still don't know how long these things take. This needed to change. By giving people a clear timeline of their residence permit application, I can make their journey much less stressful.

So I have built [a tool](https://allaboutberlin.com/guides/auslanderbehorde-wait-times) that collects reports from readers and measures wait times by department and residence permit type.

## Why I built this

I already wrote about [how predictability reduces anxiety](/projects/all-about-berlin), and how [a good map improves any journey](/blog/maps).

It's one thing not to know when your food delivery is coming, and another not to know when you will receive a regular paycheck and stop burning through your savings. A friend I was hosting ran out of money before he even got a response from the immigration office. This is not an isolated case.

Other people also have a stake in this: your dependents who came to Germany with you, and your employer who is hoping you can start working soon. People regularly lose their job because they even start due to immigration office delays.

What makes ride sharing and food delivery apps so great in my mind is that they give you an ETA. The experience of waiting is greatly improved by knowing how long you are going to wait.

Having the same sort of ETA for something as important as your right to live in this country? That would be a game changer.

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