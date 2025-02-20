---
title: Digital mise en place
description: Bringing a bit of kitchen wisdom to the digital world.
date_created: 2023-04-12
categories: golden
    technology
---

In the kitchen, you do your *mise en place* before you start cooking. You gather, measure and prepare your ingredients in advance, so that when the food hits the pan, it's all you focus on. You're not chopping a cup of red peppers while the garlic is burning, or learning that you're out of cream halfway through the recipe.

**Automation is digital mise en place**. Once you're in the flow, your scripts, shortcuts and hotkeys keep you in the flow. You're not looking for your files or trying to remember the right commands.

## Examples

I created a few commands that let me jump between projects. They put me in the right directory, set environment variables and open development tools, all with a few keystrokes. `aab -s` is a lot shorter than `cd ~/Documents/Projects/AllAboutBerlin/server && docker-compose up --build -d && cd ../site && ursus -wfs`. It's also a lot easier to remember.

I created equivalent aliases in my [SSH config](https://github.com/nicbou/dotfiles/blob/main/configs/ssh.conf). `ssh aab` is equivalent to `ssh -PXXXX root@allaboutberlin.com`.

This lets me reboot an old project without the dread of figuring out how to run it. There's a script in there that does it, and it's one of the first things explained in the README.

These tools save a few seconds here and there, sure, but above all, they help me stay focused on my main task.

## Related ideas

- [No script is too simple](/blog/no-script-is-too-simple)
