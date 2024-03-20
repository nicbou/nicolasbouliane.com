---
title: Slowing down
description: An ongoing list of things I'm doing to work less.
date_created: 2023-12-30
---

I'm too busy.

Adulthood feels like stepping onto a treadmill that never stops. If I slow down to catch my breath, I must catch up later. While I'm on vacation, chores and bills pile up, waiting for my return. Nothing is ever just *done*.

I've been at it for a while, but these days the treadmill is going too fast. My work is preordained for months, and I never get to work on what I want. Not without neglecting *something*.

Objectively, things are fine. [All About Berlin](/projects/all-about-berlin) - the website I run for a living - is steadily improving. This little [digital garden](/blog/digital-gardening) grows, flowers and bears fruit. But it's a big garden. I spend more and more time on upkeep, rarely finding the energy to plant new seeds.

I want to slow the treadmill down. I want to make more slack to build great things. This post is about how I'm doing it.

![Sleeping dog](/images/illustrations/sleeping-dog.png)

## Automation

When I was in college, I built websites for small businesses. One day during the finals, I got a call from a panicked client. Their email server was down and they were losing money. I had to set my books aside *right now* and fight that fire.

Since then, I've been exceedingly wary of creating time-sensitive work for myself. I prefer automating a job at a convenient time to being bothered at an inconvenient time. I never want to interrupt a vacation to renew an SSL certificate.

However, I still need to bite the bullet sometimes. I wrote a few important calculators that need [a yearly update in January](/blog/new-in-2024). I will update them for a third year next week. I'm getting *much* better at it. Each year, the code is a little easier to update, the tests a little more thorough. Eventually, I hope that it will mostly update itself.

There's one last task that requires a lot of maintenance: my guide on [choosing a German bank](https://allaboutberlin.com/guides/first-bank-account-in-germany). Banks frequently change their terms and update their fees, and it's a pain to rewrite the guide every few months. I'm thinking of either hiring someone to update the information, or sharing the work with other websites that have similar guides.

## Grouping

If I can't automate something, I try to do it a lot less often.

Bookkeeping is an unavoidable part of self-employment. Every month, I must ask all of my partners to send me their conversion numbers so I can issue an invoice. Then I must create the invoice, send it, and make sure that it gets paid. It's tedious work.

I convinced most of my partners to switch from monthly to quarterly invoicing. That cuts my work by two thirds. I'm considering yearly invoicing for some partners.

When I can't automate billing, I prepay long in advance. My hosting bills are covered for the next 5 years. That cuts down on bookkeeping.

## Monitoring

My main work - researching and editing guides - is fully manual. It involves monitoring dozens of topics, and updating the website when something changes. 

There is just too much to keep track of, so I use [Wachete](https://www.wachete.com/) to do it. It monitors pages for changes. I watch hundreds of pages about German law, taxes, bureaucracy and other topics. If a page changes, I get an email. This is how I keep the website up to date without losing my sanity.

I also use [Better Uptime](https://betterstack.com/uptime) to get notified if something goes wrong with the website. So far, it never happened. I'm still looking for a similar solution to monitor backups and other background tasks.

I've recently implemented "time bombs" on All About Berlin. They're little snippets that fail to compile after a certain date. Here is an example:

    This guide explains the current laws about cannabis in Germany. The rules will change in April 2024.\{\{ fail_on('2024-04-01') }}

After April 2024, this page will not build. It's a loud reminder that this page needs to be updated.

## Efficiency

I have created a small community of immigration experts. We share knowledge and answer each other's questions. It allows me to get valuable insight in minutes instead of weeks.

I also moved from a content management system to a static site generator. It completely eliminated website maintenance work, and made me much more productive when editing content. It did for my work what a sharp knife and a well laid out kitchen does for a chef's. [I wrote about it](/projects/ursus) earlier.

I'm currently thinking of ways of setting an expiration date on content. If I write "The minimum wage is 12€ (12.41€ in January)", it should trigger an error after January 1. Currently, I set calendar reminders, but it's a slow and awkward process.

## Saying no

When I started All About Berlin, I often used the line "what are they gonna do, fire me? ask for their money back?" Somewhere along the way I lost the arrogance and started taking my work much more seriously.

I often find myself in a position where helping someone costs me very little, and has a huge impact. But the costs add up, and they speed up the treadmill.

I got better at saying "no". It's harder when someone you respect has a great idea, but there just isn't enough time to do it. When I started my career I was the one pestering others for a chance, an opportunity. Now opportunities fall on my lap and I'm too damn busy to exploit them.

I know that I don't owe anyone my time and energy. I'm offering a lot of valuable information for free already. I don't feel great about declining people, but it has become a necessity.

Telling people this was a relief. I had to start telling people to find help elsewhere, and to set clear boundaries with my vacation responder. It allows me to really disconnect and unwind, and guess what... the website still runs fine!

## Doing less

More and more, I do less and less. I have shelved many projects in 2023 to stay focused on what matters to me.

I try to keep my business lean. I don't want to waste time on ceremonial aspects like printing stickers and business cards, running a newsletter, being a guest on podcasts and so on.
