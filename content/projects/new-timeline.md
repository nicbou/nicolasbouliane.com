---
title: Timeline 2.0
description: It builds a timeline out of your photos, diaries, calendars and location history. Same idea, built better.
date_created: 2023-11-28
project_url: https://github.com/nicbou/timeline
repo_url: https://github.com/nicbou/timeline
featured_image: images/timeline-1.png
categories: golden
---

Some time ago, I built a [timeline thing](/project/timeline). It ran smoothly for a few years, but it was a heavy, complex project. It was hard to configure, run, reason about and work on. I dreaded touching it.

This iteration is leaner, simpler. It's meant to be [calm technology](https://calmtech.com/) that requires as little attention as possible. It draw inspiration from the [simple, efficient static site generator](/project/ursus) I created for All About Berlin.

![Screenshot of the timeline tool](/images/timeline-2.png)

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

You run a command over some files and it outputs other files. You don't spin up a whole system with a database and an API.

I ditched Docker, Django, Django REST Framework, Postgresql, imagemagick, ghostscript, and a lot more. The new timeline is a self-contained Python package with few dependencies. You point it at files, it spits out a website.

I find this new iteration much easier to reason about. It's also easier to run and easier to maintain. I feel far more confident than people can try it out on their computer.

## Run it yourself

The code is on [GitHub](https://github.com/nicbou/timeline). It's also a Python package that you can simply install and run.

[See the project on GitHub](https://github.com/nicbou/timeline)