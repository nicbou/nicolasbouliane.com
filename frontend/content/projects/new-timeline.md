---
title: Timeline 2.0
description: It builds a timeline out of your photos, diaries, calendars and location history. Same idea, built better.
date_created: 2023-11-28
project_url: https://github.com/nicbou/timeline
repo_url: https://github.com/nicbou/timeline
categories: golden
---

On August 3, 2019, I had a crush.

You could not tell from looking at my photos. You might see Kazakh food and landscapes, and a few pictures of my mangled motorcycle. They only form part of the picture. The real story is in my notebook and my digital journal. Even my Google search history has a few hints.

I have built a tool that combines the ephemera of my life into a single timeline, that portrays my day-to-day life my life as I experience it, not just as a few photos.

![Screenshot of the timeline tool](/images/timeline-2.png)

This is my [second attempt](/projects/timeline) at such a project. The first version ran smoothly for a few years, but it was a complex mess. It was hard to configure, run, reason about and work on. I dreaded touching it.

This iteration is leaner, simpler. It's [calm technology](https://calmtech.com/). It draws inspiration from the [simple, efficient static site generator](/projects/ursus) I created for All About Berlin.

## The filesystem is the database

If I give you a database dump, you need specialised tools to peek at what's inside. If you want a nice user interface to see the data, you have to write your own.

With this project, the filesystem is the database. The data is just regular files: photos, text files, GPX tracks, etc. The timeline is just a different way to look at it.

What I like about this approach is that if the code vanishes tomorrow, I can still view those files. The static website it generates also works fine without the code that generated it.

The timeline has no data of its own. There is no database to back up, because I can always regenerate it out of the original files.

### Open standards

I tried to pick standard file formats for my data. The timeline displays images, videos and PDFs, as well as other common files. My journal is just a bunch of markdown files. My location history is GPX tracks. My search history and bank statements are in CSV files.

Common file formats are easy to work with. There are apps to view and edit those files. There is software to back them up and sync them.

I have hit a wall with certain data types for which there are no standards. For example, I'm not sure of the best way to back up tweets, Reddit comments, and private chats. There is no suitable standard format for this.

## Scripts over systems

Nowadays I prefer to work with scripts. I run a command over some files and it outputs other files. I don't like spinning up a whole system with a database and an API.

This iteration has far fewer moving parts. I ditched Docker, Django, Django REST Framework, Postgresql, imagemagick, ghostscript, and a lot more. It's a self-contained Python package with few dependencies. You point it at files, it spits out a simple static website.

This is much easier to reason about, run and maintain.

## Run it yourself

The code is on [GitHub](https://github.com/nicbou/timeline). It's also a Python package that you can simply install and run.

[See the project on GitHub](https://github.com/nicbou/timeline)