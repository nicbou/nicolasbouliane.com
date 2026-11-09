---
title: Home server
description: I built a movie streaming server. My friends dubbed it "Nickflix".
date_created: 2019-05-13
project_url: https://home.nicolasbouliane.com
repo_url: https://github.com/nicbou/homeserver
featured_image: images/Home-page.jpg
---

Over a decade ago - before Netflix reached our shores - I had hundreds of movies on a computer in my living room. They were in a disorganised directory. Picking a movie was an exercise in frustration, so I set to build a tool that would organise my collection.

At first, it was a simple page that listed the media files, and launched VLC when you clicked one. Through several iterations, it became closer to a personal Netflix. I added covers, authentication, automatic triage, subtitle extraction, support for episodes and seasons, streaming, Chromecast support, and a party mode.

This is my longest-running project, and one of my favourites. It runs smoothly, but I still find things to add to it.

## What it does

When a torrent is finished downloading, the media files show up in the triage pile. On the triage page, I match the files to movies or TV shows. The server pulls the movie title, description and poster from TMDb, and adds it to the library.

In the background, the media files are renamed and moved to a neatly organised folder, along with the poster and the subtitles. The movie is converted to .mp4, and the subtitles are [extracted and converted](/blog/ffmpeg-extract-subtitles). This way, every movie can be streamed in a browser, on a Chromecast, or on any other device.

Everything is locked behind a login prompt. I have an administrator account, and many of my friends have user accounts. They can watch movies, but also star them, and keep track of which movies they've seen and not seen. If they return to a movie, the player remembers where they left off.

## How it does it

In its current iteration, the home server is a [VueJS](https://vuejs.org/) frontend, a Django backend and an [rq](https://python-rq.org/) conversion pipeline. The conversion pipeline uses ffmpeg to convert the movies to H.264 and extract the subtitles. I get movie information and posters from the [TMDb API](https://developers.themoviedb.org/3). Everything runs inside Docker containers on my home server.

![Home page](/images/Home-page.jpg)

![Episodes](/images/Episodes.png)

![Player](/images/Player.jpg)

![Triage](/images/Triage.jpg)

