---
title: Digital mise en place
description: Bringing a bit of kitchen wisdom to the digital world.
date_created: 2023-04-12
---

In the kitchen, you do your *mise en place* before you start cooking: you gather, measure and prepare your ingredients in advance, so that once the food hits the pan, it's all you focus on. You're not chopping a cup of paprika while your garlic is burning, or finding halfway through the recipe that you ran out of cream.

**Automation is digital mise en place**. Once you're in the flow, your scripts, shortcuts and hotkeys let you stay in the flow. It's not so much about saving time, but about staying focused on your main task.

## Examples

The `project` command in my [dotfiles](https://github.com/nicbou/dotfiles) launches a project. It puts me in the right working directory, launches docker and opens my IDE. It's roughly equivalent to...

```bash
cd /.../AllAboutBerlin/source \
&& docker-compose up --build -d \
&& open -a 'Sublime Text' ./
```

For my most common projects, I set up even shorter aliases like `aab` for All About Berlin, `hs` for my home server, `nb` for my personal website, and `tl` for my timeline thing. Three keystrokes and I'm back to work.

I have equivalent aliases in my SSH config, so that `ssh aab`, `ssh hs` and `ssh nb` connect to the right servers.

When these tools are missing, I find myself [shaving yaks](https://www.mindprod.com/jgloss/yakshaving.html). I lose my train of thought while clicking around an admin interface or navigating to a directory in the command line.

## Related ideas

- [No script is too simple](https://nicolasbouliane.com/blog/no-script-is-too-simple)

