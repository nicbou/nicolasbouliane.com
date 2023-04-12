---
title: How to clear the nginx static cache
description: This is how you clear the nginx fastcgi cache or proxy cache without restarting nginx.
date_created: 2022-03-15
---

This is how you clear the nginx fastcgi cache or proxy cache.

First, find the path to your static cache files. In your nginx config, you should have a `fastcgi_cache_path` or `proxy_cache_path` set. For example, this is mine:

```
# /etc/nginx/nginx.conf
fastcgi_cache_path /var/run/nginx-cache/craftcache levels=1:2 keys_zone=craftcache:100m [...];
```

My static cache path is `/var/run/nginx-cache/craftcache`. To clear the static cache, I must delete the contents of this directory, but not the directory itself:

```bash
# Correct - this deletes the cache files, but not the cache directory
rm -rf /var/run/nginx-cache/craftcache/*

# Wrong - this deletes the cache directory and requires an nginx restart
rm -rf /var/run/nginx-cache/craftcache
```

## Clearing the nginx cache inside docker

If you run nginx inside docker, the wildcard is [interpreted on the host](https://stackoverflow.com/questions/42767588/docker-exec-rm-not-working), not inside the container. It will not delete any files. You must do it this way:

```bash
# Correct - this will clear the cache
docker-compose exec your_nginx_container sh -c 'rm -rf /var/run/nginx-cache/craftcache/*';

# Wrong - this will not delete any files
docker-compose exec your_nginx_container rm -rf /var/run/nginx-cache/craftcache/*;
```

## tl;dr

```bash
rm -rf /var/run/nginx-cache/craftcache/*
```

