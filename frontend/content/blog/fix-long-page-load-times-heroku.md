---
title: How to fix long page load times on Heroku
description: 
date_created: 2013-11-15
---

If you have a free Heroku instance, you might sometimes face a long first page load time on your web application. This is because Heroku will shut down your instance after a while if nobody visits your site. This is a problem I have encountered with [Bill Splitter](/projects/bill-splitter/) since my girlfriend and I were the sole users.

There is a simple way to fix that: **curl or wget the website every few hours**. You can place the command in a cron job and you will never deal with a slow first page load again.

It's not the nicest thing to do since you are abusing a free service, but it does fix the problem.

