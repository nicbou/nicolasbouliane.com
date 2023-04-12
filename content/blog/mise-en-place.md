---
title: Digital mise en place
description: Bringing a bit of kitchen wisdom to the digital world.
date_created: 2023-04-12
---

In the kitchen, you do your *mise en place* before you start cooking: you gather, measure and prepare your ingredients in advance, so that once the food hits the pan, it's all you focus on. You're not chopping a cup of paprika while your garlic is burning, or learning that you're out of cream halfway through the recipe.

**Automation is digital mise en place**. Once you're in the flow, your scripts, shortcuts and hotkeys keep you in the flow. It's not so much about saving time, but about staying focused on your main task.

## Examples

The `project` command in my [dotfiles](https://github.com/nicbou/dotfiles) launches a project: it puts me in the right directory, launches docker, opens my IDE, etc. For most projects, it's roughly equivalent to...

```bash
function allaboutberlin {
    cd /.../AllAboutBerlin/source \
    && docker-compose up --build -d \
    && open -a 'Sublime Text' ./
}
```

For the most common project, I set up short aliases. `aab` is equivalent to `project AllAboutBerlin`, and `hs` is equivalent to `project HomeServer`. It lets me hop between projects in a few keystrokes.

I created equivalent aliases in my [SSH config](https://github.com/nicbou/dotfiles/blob/main/configs/ssh.conf). `ssh hs` is equivalent to `ssh -PXXXX home.nicolasbouliane.com`.

I have [other aliases](https://github.com/nicbou/dotfiles/blob/main/dotfiles/aliases.sh) for common commands, such as `dcubd` for `docker-compose up --build -d`.

When these tools are missing, I find myself [shaving yaks](https://www.mindprod.com/jgloss/yakshaving.html). I lose my train of thought while clicking around an admin interface or navigating to a directory in the command line.

## Related ideas

- [No script is too simple](https://nicolasbouliane.com/blog/no-script-is-too-simple)

