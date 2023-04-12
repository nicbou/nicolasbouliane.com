---
title: No script is too simple
description: I write very short scripts, sometimes for single-line commands. Here's why you should do it too.
date_created: 2020-09-18
---

Most of the projects I work on have a `scripts` directory. For example, here's are the scripts I use for [All About Berlin](https://allaboutberlin.com/):

```
backup-db.sh
clear-static-cache.sh
copy-production-db.sh
restore-db.sh
save-composer-dependencies.sh
```

Those scripts are all pretty simple. They're under 10 lines long and take no arguments. Some just call a single command, so why bother creating them? Because they are [digital mise en place](/blog/mise-en-place)

## One task, one way

*What* must be done ("start the project", "run the tests" etc.) won't change. *How* it must be done ("yarn ...", "docker-compose ...") can change multiple time in a project's lifespan. **It's a lot easier to update a single script than to propagate a new set of commands**.

This script contains the only valid instructions for starting the project. **It's the single source of truth for how to perform that task**. Your colleagues, your CI/CD pipeline, your commit hooks, your cronjobs, your other scripts and your documentation can just refer to `start.sh`. If you change the script, the new instructions propagate instantly. You don't need to inform your colleagues, update a bunch of Jenkins jobs or update the README. All of it is still up to date. There will be no discrepancies.

With all those people and machines working off the same scripts, it pays to improve them. You can add usability improvements that will benefit the whole team. You can check the python/node/docker versions, add error handling, remove noise from the output, add colours and headers to build steps, and even interactivity.

**Script calls are also more explicit than commands**. A Jenkins job that calls ```lint-source.sh && start.sh && run-tests.sh && ...` is pretty self-explanatory. A script called `create-user.sh` is easier to remember than `docker-compose exec backend python3 manage.py createsuperuser`. This is especially nice when you frequently switch between projects, and constantly need to recall how each one works.

