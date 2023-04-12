---
title: Digital mise en place
description: 
date_created: 2023-03-25
---

In the kitchen, you always do your *mise en place* before you start cooking. You gather, measure and prepare your ingredients in advance, so that once the oil meets the pan, your full focus is on what's in it. You're not chopping a cup of paprika while your garlic is burning, or finding halfway through the recipe that you're out of cream.

**Automation is digital mise en place**. Once you're in the flow, your scripts, shortcuts and hotkeys let you stay in the flow. It's not so much about saving time, but about preserving your focus for your main task.

For example, the `project` command in my dotfiles launches a project. It puts me in the right working directory, launches docker and opens Sublime Text. It's roughly equivalent to...

```bash
cd /.../AllAboutBerlin/source \
&& docker-compose up --build -d \
&& open -a 'Sublime Text' ./
```

For my most common projects, I set up even shorter aliases like `aab` for All About Berlin, `hs` for my own server, `nb` for my personal website, and `tl` for my timeline thing. I'm always a few keystrokes away from a working development environment.

...

To edit a page on All About Berlin, I have to log into the admin area, navigate to the list of entries, and select the one I want to edit. I wrote a bookmarklet that does this in a few keystrokes. I just type `edit` in the address bar, and it opens the page editor in a new tab.

...

When these tools are missing, I find myself [shaving yaks](https://www.mindprod.com/jgloss/yakshaving.html). I lose my train of thought while clicking around an admin interface or navigating to a directory in the command line.

## Related ideas

- [No script is too simple](https://nicolasbouliane.com/blog/no-script-is-too-simple?token=xrZ9cZNEXRFvmZL9edD0IOjDPGlajQAc)

