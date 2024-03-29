---
title: Timeline v2
description: It builds a timeline out of your photos, diaries, calendars and location history. Same idea, built better.
date_created: 2023-11-28
project_url: https://github.com/nicbou/timeline
repo_url: https://github.com/nicbou/timeline
---

A few years ago, I have built a [timeline thing](/project/timeline). It has been running smoothly on my home server since then, but I dread touching it.

It's a heavy project. It's hard to configure, hard to run, hard to reason about, hard to work on, and hard to monitor.

All About Berlin used to be like this, until I migrated to a [simple, efficient static site generator](/project/ursus). It had a profound positive impact on my workflow. I applied lessons from this migration to the timeline thing.

This iteration is meant to be calm technology. It's meant to just work and to require as little attention as possible.

Here's roughly how I did it.

## The filesystem is the database

If I give you a database dump, you need a few specialised tools to peek at what's inside. If you want a nice user interface to see the data, you'll likely have to write your own.

My websites used to have big databases like that. To read those, I had to set up an elaborate software project with gigabytes of dependencies: docker, PHP, MySQL, some content management system... what a pain!

Now these websites are just a collection of markdown files. Each page is a plain text file in a folder. It's easy to reason about the site structure, and to edit the content with the software I want.

I didn't want this timeline to be a complex system with a cryptic database. I wanted it to be just another way to visualise my personal files. I wanted to point it at a bunch of folders and say "make a timeline out of this".

One benefit to that approach is that the timeline has no data of its own. I don't have to back up its database, because I can always rebuild a timeline out of the original files.

### Open standards

I tried to pick standard file formats for my data. The timeline displays images, videos and PDFs, as well as other common files.

The main benefit is that I can use any software I want to view and edit the data. My location history is just a bunch of GPX files. There are many ways to view and edit those. I can even load them on my GPS device and share them with friends.

For certain data there are no standards, and that's challenging. I have years of chat history and no suitable file format to store them.

## Scripts over systems

You run a command over some files, instead of spinning up a whole system.

I ditched Docker, Django, Django REST Framework, Postgresql, imagemagick, ghostscript, and a lot more. The new timeline is a self-contained Python package with few dependencies. You point it at files, it spits out a website.

All in all, it's a lot easier to reason about. It's easier to use and easier to maintain. I feel far more confident than people can try it out on their computer.