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

## The filesystem is the database

If I give you a database dump, you need a few specialised tools to peek at what's inside. If you want a nice user interface to see the data, you'll likely have to write your own.

My websites used to have big databases like that. To read from these databases, I had to set up an elaborate software project with gigabytes of dependencies: docker, PHP, MySQL, some content management system... what a pain!

Now these websites are just a collection of markdown files. Each page is a plain text file in a folder. It's easy to reason about the site structure, and to edit the content.

I didn't want this timeline to be a complex system with a cryptic database. I wanted it to be just another way to visualise my personal files. I wanted to point it at a bunch of folders and say "make a timeline out of this".

One benefit to that approach is that the timeline has no data of its own. I don't have to back up its database, because I can always rebuild a timeline out of the original files.

### Open standards

I tried to pick standard file formats for my data. The timeline displays images, videos and PDFs, but it also gets my geolocation history from GPX files.

For certain data there are no standards, and that's challenging. I have years of chat history and no suitable file format to store them.

## Scripts over systems

There is no longer a system. It's just a script.

I ditched Docker, Django, Django REST Framework, Postgresql, imagemagick, ghostscript, and a lot more. The new timeline is a self-contained Python package with few dependencies.

There is no longer an elaborate instruction set to run the project. You no longer need to spin up half a dozen Docker images to achieve that. You call `timeline` and you get a timeline. It's that simple. 

For the first time, I feel confident that other people can run this project too. People did run the old timeline and even submitted pull requests to it, but that's a statement to their dedication, not to the project's usability.