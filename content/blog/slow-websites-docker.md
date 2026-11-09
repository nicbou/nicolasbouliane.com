---
title: Why Docker for Mac is making your website slow
description: My website was painfully slow in Docker on my OS X machine, but really fast in production. I found why.
date_created: 2020-05-04
---

When I was rebuilding my personal website, pages loaded extremely slowly, especially in the Craft CMS admin. This was odd, since it used the exact same stack as [All About Berlin](https://allaboutberlin.com/), which is ridiculously fast.

## Is this your problem?

- Do you use Docker for Mac?
- Do you mount your website's code or static assets as a volume?
- Is your website is *very* slow on your machine, but fast in production?

If that's the case, your problem is probably the same as mine.

## The problem and the solution

**Volumes in Docker for Mac are really slow**. [This is a known issue](https://docs.docker.com/docker-for-mac/osxfs-caching/#performance-implications-of-host-container-file-system-consistency). When your Docker machine accesses files on a mounted volume, it slows everything down. If your website's scripts or static assets are in a volume, your pages will load slowly.

In my case, Composer's vendors directory was in a volume, so every page load touched a dozen PHP files very slowly. On my other websites, the vendors directory was in a different location.

The solution is to copy files onto the docker machine, instead of mounting them as a volume. There are [other ways](https://docs.docker.com/docker-for-mac/osxfs-caching/#performance-implications-of-host-container-file-system-consistency) to make volumes faster on OS X, depending on your situation.

