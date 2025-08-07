---
title: Building an insurance case tracker
description: Our first step towards building an insurance business.
date_created: 2025-08-06
categories:
    allaboutberlin
---
[As mentioned previously](/blog/health-insurance), we're building an insurance business from the ground up, starting with a case tracking system. This will allow us to follow a customer's journey from their first email to their coverage confirmation.

## Why start with a case tracker?

We must do this for a few reasons.

First, so that nothing gets lost. A few months ago, I started asking people for feedback, and learned that a few of them had never heard back from the broker. I want to make sure that every question gets answered, and that no customer falls through the cracks. Tracking cases might help us troubleshoot our [abandonment rate](https://en.wikipedia.org/wiki/Abandonment_rate).

Second, by mapping out the customer's journey, we can measure and improve it. We can see where things take too long, and where people get stuck and give up. We can find ways to reduce friction and speed things up. We should not schedule a phone consultation in a week when we can solve someone's problem in five minutes with a template email.

Third, it lets us track outcomes. I want to know which customers got which insurance, so that I can explain these things on [All About Berlin](https://allaboutberlin.com/guides/german-health-insurance). For example, if foreign students always end up with the same health insurance, we can recommend it right away and skip a labour-intensive consultation. That knowledge will serve a lot more people if it's right there on the internet. I think that we will also find all sorts of little details that would escape us otherwise. Maybe one insurer's payment methods don't mesh well with parts of our audience or maybe their onboarding process is too frustrating. In any case, it's information that will help us do a better job.

## How I'm building it

We started mapping things out on a whiteboard. We narrowed the process down to a few stages: *new*, *in progress*, *waiting* and *done*. There are nine possible statuses in total, but they roughly fit in those four categories.

![The possible states of an insurance case](/images/insurance-case-tracking-model.jpg)

The case's status is not just a field that you update like a cell in a spreadsheet. We log each status change along with the date. This lets us look at each case as a timeline: two hours to first reply, maybe a week of back and forth with the customer, and two weeks of waiting for the health insurer. This is helpful information.

If a case has been "waiting" for a month, we want to prioritise it over others, and maybe shoot someone an automated reminder to get things moving again. When we look at all those timelines in aggregate, we can see where things take too long and find ways to improve it.

One problem that we identified early on is that we waited too long to collect basic information. Some people have pretty straightforward cases, and if we knew a little more about them up front, we could skip the consultation call and get them insured within 24 hours. Instead it takes us a few days and a phone call to achieve the same thing. Soon we will have a far better idea of which parts of the process we can improve.

Beyond that, there is nothing special. We have a bit of information, and we can add comments and files to the case over time. If you have seen Jira or HubSpot, none of this will blow your mind.

## Technically speaking

I chose to build this case tracker in Django, because it's what All About Berlin's backend uses, and it's perfect for the job. I just had to create the database models and turn on Django Admin, and bam, instant case tracking software. It took about two days to get everything up and running. We can immediately start feeding new cases into it and see what we can learn from it.

We could use HubSpot or something similar for this, and that would get us 90% of the way really quickly, but I think the real success is in those last 10%. This is where we get to be creative and innovate. If we control the platform and the code our business runs on, we can truely adapt it to our need, instead of the other way around.

We are not bound by the limited imagination of SaaS platform developers. We also get to build a neat, fast, privacy-friendly little platform instead of mashing together a bunch of expensive apps. Best of all, it will run on our existing hardware at no extra cost.