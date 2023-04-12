---
title: How to fix an accidental Nextcloud docker image update
description: Here's what to do if you get "Updates between multiple major versions and downgrades are unsupported" after updating the docker image.
date_created: 2020-12-10
---

## The problem

I run Nextcloud in a docker container with the official `nextcloud` docker image. By default, this builds the *latest* Nextcloud image.

I was using the Nextcloud 18 image. When I rebuilt my docker-compose project after a long time, it downloaded the Nextcloud 20 image. My Nextcloud database was at version 18, but the Nextcloud code was now at version 20. Nextcloud does not allow skip a major version when you update (18 to 20). I saw this error when I tried to turn off maintenance mode and upgrade manually:

```
Updates between multiple major versions and downgrades are unsupported. Update failed
```

I tried to roll back to Nextcloud 18 by using the `nextcloud:18` docker image and running `docker-compose up --build -d`, but it didn't work. The container kept rebooting with the following error message:

```
Can't start Nextcloud because the version of the data (20.0.2.2) is higher than the docker image version (18.0.11.2) and downgrading is not supported. Are you sure you have pulled the newest image version?
```

## The solution

Make sure you're using the newer Nextcloud image, the one you upgraded to by accident. Otherwise the container will be stuck in a reboot loop, and you won't be able to access it.

**First**, we need to know what version we *used* to have.

```
# My docker image is called "nextcloud-php"
docker-compose nextcloud-php cat config/config.php | grep version
```

This will show you out the version number you had *before*. Mine was 18.0.4.2.

**Second**, you must fix `version.php` to use the old version (18.0.4.2).

The upgrade to Nextcloud 20 failed, but `version.php` was updated anyway, so Nextcloud thinks it's at version 20. That's why you got an error message when you rolled back to the old version.

To do this, you will need a text editor. The `nextcloud` image does not have vi, vim or nano.

```
docker-compose nextcloud-php apt-get update \
    && apt-get install nano \
    && nano config/config.php
```

Change `config.php`. Put your old version wherever it fits, and save your changes (Ctrl + X, Y, Enter).

```
<?php
$OC_Version = array(18,0,11,2); // <----- HERE!
$OC_VersionString = '18.0.11.2'; // <----- HERE!
$OC_Edition = '';
$OC_Channel = 'stable';
$OC_VersionCanBeUpgradedFrom = array (
  'nextcloud' =>
  array (
    '17.0' => true, // <----- HERE! Set it to your major version minus 1 (18.0.4.2 -> 17.0)
    '18.0' => true, // <----- HERE! Set it to your major version (18.0.4.2 -> 18.0)
  ),
...
```

**Third**, you must downgrade to your old Nextcloud version. Change your docker-compose file to use the `nextcloud:18.0.4` image, instead of `nextcloud`. Run `docker-compose up --build -d` again. You should now be on Nextcloud 18, and the container should start properly. However, it will be in maintenance mode, and even if you turn it off, you might have issues.

**Fourth**, you must upgrade *one* major version. For example, from 18 to 19. Just change the version of the docker image, for example from `nextcloud:18.0.11` to `nextcloud:19`. Run `docker-compose up --build -d` again. You might need to turn the maintenance mode off yourself:

```
docker-compose nextcloud-php php occ maintenance:mode --off
```

Your Nextcloud install should now work properly.

**Fifth**, you might want to keep incrementing the docker image version until you have the latest major version of Nextcloud. In the future, either used a fixed version of the `nextcloud` image, or don't wait so long before updating the image.

