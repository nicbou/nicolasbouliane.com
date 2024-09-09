---
title: Ursus
description: The static site generator that powers this website and All About Berlin. Written in Python.
date_created: 2023-04-12
repo_url: https://github.com/all-about-berlin/ursus/
---

I built a static site generator for [All About Berlin](https://allaboutberlin.com/). It also powers my personal website. It's open source; you can find the code on [Github](https://github.com/nicbou/ursus/).

{% include "blocks/_tableOfContents.html" %}

## A what?

A static site generator. It turns a bunch of text files into a website.

All About Berlin once ran on [Craft CMS](https://craftcms.com/), which is a bit like WordPress. To make changes, I logged into the admin area, made changes with a rich text editor, and saved them to a database. The server rendered the database content into pages.

Now the content is a bunch of markdown files on my computer. When I run a command, they're turned into a website. In other words, instead of generating pages on demand on the server, I generate them in advance, on my laptop.

## Why a static site generator?

A static site generator has many benefits over a content management system. Many of those are specific to how I work.

### Work offline

The entire website is on my computer. I can make changes and preview them without an internet connection. I can deploy the changes later, when I'm back online.

This lets me work in more interesting places, where reliable internet is not guaranteed. This lets me spend more time away from my desk.

### Lightweight server

Static websites are just a bunch of files: HTML pages, images, and a few PDFs. The server returns pre-rendered pages, instead of building them on the fly.

This requires a far simpler server with far fewer moving parts. There is no PHP interpreter, no heavy database, and no elaborate caching mechanism. This means less code to run, less software to keep updated, and fewer things a hacker can exploit.

Just look at the server load before and after the migration to Ursus.

![Resource usage before and after the deployment](/images/illustrations/allaboutberlin-before-after.jpg "The day the fans fell silent")

A lightweight server runs smoothly on older hardware, like the laptop I usually work on. The old setup would bring it to a crawl and halve its battery life.

### Bring your own tools

My content was locked in a database that only Craft CMS could work with. I could only edit the content with the tools Craft CMS gave me. Those tools were rather restrictive.

Now the content is a bunch of text files. I can edit and transform them with an endless arsenal of tools. Those are the tools I've been using for over a decade: Sublime Text, grep, sed, git, etc. I even wrote a few myself, such as content linters and link checkers.

I can apply fixes across hundreds of pages with regular expressions. Changes that were once too tedious to even consider now take a few seconds. Even simple things like linking to other pages became so much easier with Sublime Text's autocomplete.

For example, it's now easy to replace "permanent residency" with "permanent residence", move thousands of footnote superscripts [after the punctuation mark](https://tex.stackexchange.com/questions/56063/how-to-properly-typeset-footnotes-superscripts-after-punctuation-marks), or fix hundreds of broken links.

### What you see is what you mean

Craft's rich text editor had many quirks:

- It randomly inserted empty `<a>`, `<strong>`, and `<sup>` tags.
- It [deleted all links on a page](https://github.com/craftcms/redactor/issues/331#issuecomment-869557385) if I looked at it wrong. If I didn't notice in time, I'd have no way to revert it.
- It inserted a lot of invisible characters like non-breaking spaces and byte order marks. Some of those characters spread into titles and file names, and were a royal pain to get rid of.
- It collapsed indentation on code blocks. They fixed it, but the damage was done.

Markdown is a lot more reliable. It renders as you expect it to, with no surprises.

### Make your own build

All About Berlin is now a pipeline. Markdown files enter one end, and a website comes out the other. What happens in the middle is entirely up to me.

I convert images to .webp files of different sizes, so that they load faster. I generate thumbnails for PDF files. I create an offline index to make the search absurdly fast. I also wrote linters that look for dead links, unused images, spelling mistakes, etc.

I'm not constrained by what the creators of Craft CMS thought I might want. If I can script it, it can happen.

## Why not sooner?

### Just editing

I like pressing Cmd + S and seeing the changes go live. I want to *write* content, without *building* and *deploying* it.

With Craft, I just navigated to allaboutberlin.com/admin and got to work. With Ursus I have to open a terminal and type a few commands.

On the other hand, opening and editing markdown files is *much* faster than clicking through Craft's admin area. The cost of starting the project is offset by the insane efficiency gains when editing content.

### No suitable options

Existing static site generators seemed focused on simple blogs. They did not support complex relationships between entries (related content, reviewers, glossary entries, attachments). It was also impossible to insert tools and widgets in the content. I didn't want to rebuild my website around another tool's limitations, so I wrote my own.

I ended up extending both Markdown processing and Jinja template rendering to suit my needs. This would have been much harder if I picked a different tool written in an unfamiliar language.

### Markdown limitations

Markdown has some important limitations:

- No support for image captions
- No way to embed widgets in the content (like my [tax calculator](https://allaboutberlin.com/tools/tax-calculator))
- No support for variables and constants in the content

I had to [extend Python Markdown](https://github.com/all-about-berlin/ursus/blob/master/ursus/context_processors/markdown.py) to support those things.

## Building the static site generator

### Rebuilding on content changes

Sometimes multiple files changed in succession, triggering a dozen subsequent rebuilds.

Sometimes multiple files changed while the website was already being rebuilt, triggering multiple subsequent rebuilds instead of just one.

The rebuild was slow at first, because it rebuilt all 400 pages. It took about 14 seconds. I brought it down to around 4 seconds.

## Migrating the content

I used [html-to-markdown](https://github.com/thephpleague/html-to-markdown) to convert the existing HTML content to markdown.

I modified the Craft templates to return fully formatted Markdown files instead of a nice HTML page, then saved each page.

This worked really well, although I had to fix a few things manually. At this point I was working with text files, so I had a lot of powerful tools at my disposal.

### Content

I had to fix 5 years of garbage HTML created by Craft's rich text editor. Those included a lot of empty HTML tags. I fixed most of them with find-replace, but eventually, I had to manually verify each of the 400 pages.

### Widgets

In-content widgets like my health insurance calculator were replaced by a Jinja include statement. Those are handled by Ursus.

```markdown
This guide is for tourists who want to visit Berlin. If you want to move to Berlin, read my [moving to Berlin guide](https://localhost/guides/moving-to-berlin).

{% raw %}{% include "blocks/_tableOfContents.html" %}{% endraw %}

## Visa requirements

You might need a visa to visit Germany. It depends on your citizenship: ...
```

### Sources

Those used to be numbered links in `<sup>` tags. I wrote a custom Craft filter that turned them into [markdown footnotes](https://python-markdown.github.io/extensions/footnotes/).

```markdown
Before: A well-sourced statement in Craft<sup><a href="sourceA">1</a>, <a href="sourceB">2</a></sup>.

After: A well-sourced statement in Markdown.[^statementA]

...

[^statementA] <https://...>, <https://...>
```

The new footnotes combine multiple sources into a single footnote. This<sup>1</sup> is a lot less distracting than this<sup>1, 2, 3, 4</sup>. The new footnotes also allow comments, instead of just linking to other pages.

![Footnotes on All About Berlin](/images/allaboutberlin-footnotes.png)

### Search

With no server to index pages and handle search, I had to rewrite search from scratch.

I generate an index with Lunr.py, and use Lunr.js in the browser to search content. It's ridiculously fast, and a massive user experience improvement. [Try it yourself.](https://allaboutberlin.com/guides)

## How it feels

All About Berlin has been running on Ursus for a while now. I am very happy with the results. I spend a lot less time babysitting the server. Writing content with a powerful text editor feels a lot more natural for a software developer.

After two months, I decided to move my personal website to Ursus.