---
title: Having issues with your first Django deployment on Heroku?
description: 
date_created: 2013-12-07
---

After spending a part of the night swearing at Heroku for not seeing my Django app correctly, I have realized it requires a very specific folder structure to operate properly.

In my case, my whole Django project was in a subdirectory of my git repo (`git_root > django_project > django_project > settings.py`), while Heroku expects the following structure: `git_root > django_project > settings.py`.

Some other problems I have encountered:

- Make sure you have everything you need in your requirements.txt file
- Add your Procfile and requirements.txt to git
- Don't forget to run syncdb on the server: `heroku run python manage.py syncdb`

Still in a tough spot? Use `heroku logs` to figure out what's going on. If you don't see any error message, try `heroku restart`. It will usually generate a few errors to work from.

