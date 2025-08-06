---
title: Building an insurance case tracker
description: Our first step towards building an insurance business.
date_created: 2025-08-06
categories:
    allaboutberlin
---
[As mentioned previously](/blog/health-insurance), we're building an insurance business from the ground up, starting with a case tracking system. This will allow us to follow a customer's journey from the moment the email us until they are covered.

## Why start with a case tracker?

We must do this for a few reasons.

First, so that nothing gets lost. A few months ago, I started asking people for feedback, and learned that a few of them had never heard from our broker. I want to make sure that every question gets answered, and that no customer falls through the cracks. Tracking cases might help us diagnose and improve our [abandonment rate](https://en.wikipedia.org/wiki/Abandonment_rate).

Second, by mapping out the customer's journey, we can measure and improve it. We can see where things take too long, and where people get stuck and give up. We can find ways to streamline things and solve their problem faster. We should not schedule a consultation a week later when we can solve the same problem with a template email within five minutes.

Third, it lets us track outcomes. I want to know which customers got which insurance. If we can find common patterns, we can simplify things. For example, if foreign students always end up with the same health insurance, we can recommend it right away, without scheduling a video call. If I put that information right on All About Berlin and my health insurance calculator, this information can reach even more people.

## How I'm building it

We started mapping things out on a whiteboard. We narrowed the process down to a few stages: *new*, *in progress*, *waiting* and *done*. When our broker logs in in the morning, that's what he wants to know. There are nine possible statuses in total, but they roughly fit in those four categories.

![The possible states of an insurance case](/images/insurance-case-tracking-model.jpg)

The status is not just a field that you toggle like a cell in a spreadsheet. We log each status change with the date. This lets us look at each case as a timeline: two hours to first reply, maybe a week of back and forth with the customer, and two weeks of waiting for the health insurer.

If a case has been "waiting" for a month, we want to prioritise it over others, maybe shoot some automated reminders to get things moving again. When we look at all those timelines in aggregate, we can see where things take too long and find ways to improve it.

One problem that we identified early on is that we waited too long to collect basic information. Some people have pretty straightforward cases, and if we had that information up front, we could skip the consultation call and get them insured within 24 hours. It removes a lot of friction, and people notice that.

## Technically speaking

I chose to build this case tracker in Django. I just had to create the models and turn on Django Admin, and bam, instant case tracking software. It took about two days to get everything up and running. We can immediately start feeding new cases into it and see what we learn from it.

We could use HubSpot or something similar for this, and that would get us 90% of the way really quickly, but I think the real success is in those last 10%. This is where we get to be creative and innovate. If we control the platform and the code our business runs on, we can really adapt it to our taste. We are not bound by the limited imagination of SaaS platform developers.