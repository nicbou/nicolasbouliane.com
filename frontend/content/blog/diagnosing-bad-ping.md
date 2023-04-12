---
title: Diagnosing a bad ping
description: How to find out why you have a bad ping
date_created: 2014-07-25
---

Once in a while, you will deal with an unbearably long ping time. Calling your ISP might solve the problem after a few minutes of trial and error, but it's usually after spending a few hours on the phone. Here is a short list of things you should check before calling:

## Step 1: Gathering data

First, let's see whether it's you or the ISP:

1. Look at your ISP's Twitter and status page. It's a low effort way to see if other people are having the same issue.
2. Reboot your modem and router and try plugging your computer to the modem directly. Sometimes, it's the simple stuff.
3. Check your ping immediately after rebooting your router and modem. In a recent case, the ping was fast for a minute or two after rebooting, then slowed to a crawl. A service on my server was hogging my bandwidth as soon as it had internet access.
4. Ping from different devices. If you can get a good ping on a wired device but not on a wireless one, it might be a signal problem.
5. Check your router's status page. If you run DD-WRT, you can see the bandwidth usage and connection strength. In a recent case, I could see that a wired device was hogging the bandwidth.

## Step 2: Common culprits

If you have figured that the problem is on your side, here are some common problems to look for.

1. Check your torrents. If your upload rate matches that of your internet connection, it can slow the internet down to a crawl. Don't forget to convert kilobytes to kilobits when comparing.
2. Check your services. If you are running services (VPN, proxy, web server, SSH etc), check if they are being attacked or used without consent. I once foolishly ran a public proxy that somehow made its way onto a public proxy list and it killed my router after a few minutes. The Apache access logs, among other things, might provide some information.
3. Check your other computers. On OS X, use the Network tab in Activity Monitor to spot bandwidth hogs. The Windows task manager offers similar functionality.

