---
title: Automated cache clearing on All About Berlin
description: How I automatically purge pages from the cache when they are saved.
date_created: 2022-12-22
---

All About Berlin uses caching heavily. Serving cached pages is much faster than generating them on the fly on every request. It makes the website snappy, and reduces the server load dramatically.

I want to cache pages for as long as possible to lighten server load, but I want the changes I make to go live instantly. Simple enough, right?

> "There are only two hard things in Computer Science: cache invalidation and naming things."

> — Phil Karlton

## The goal

When I wear my editor hat, I only want to deal with editing matters. There shouldn't be a series of steps to "deploy" content. It should go live when I hit "save". Fiddling with the terminal or the Cloudflare dashboard to clear the cache is an unwelcome distraction.

## How I did it

A page is cached in two places:

- in the local nginx FastCGI cache
- on Cloudflare's servers.

When I save a page, I purge its cached copy from both places.

### Triggering the purge

I created a Craft CMS module that intercepts the `EVENT_BEFORE_SAVE` event. It gets the entry's URL, and purges it from the cache.

```php
Event::on(
    Entry::class, 
    Element::EVENT_BEFORE_SAVE,
    function(ModelEvent $e)
    {
        $entry = $e->sender;
        if (ElementHelper::isDraftOrRevision($entry)) {
            return;
        }
        $this->purgeFromCache([$entry->getUrl()]);
    }
);
```

Tags were a bit more work, because [they don't have a URL](https://craftcms.com/knowledge-base/assigning-urls-to-tags). I had to use hard-coded logic to get their URL. It makes the module less reusable, because it's now coupled to All About Berlin's structure. Using tags for [glossary entries](https://allaboutberlin.com/glossary) was a mistake.

```php
Event::on(
    Tag::class,
    Element::EVENT_BEFORE_SAVE,
    function(ModelEvent $e)
    {
        $tag = $e->sender;
        if (ElementHelper::isDraftOrRevision($tag)) {
            return;
        }
        $tagUrl = App::parseEnv('@web') . "/glossary/" . rawurlencode($tag->title);
        $tagUrlJson = $tagUrl . "/json";
        $this->purgeFromCache([$tagUrl, $tagUrlJson]);
    }
);
```

So far, so good. It clears a page from the cache when it changes.

Here is the module's full code:

```php
<?php

namespace modules\cachepurge;

use Craft;
use craft\base\Element;
use craft\elements\Entry;
use craft\elements\Tag;
use craft\events\ModelEvent;
use craft\events\TagGroupEvent;
use craft\helpers\App;
use craft\helpers\ElementHelper;
use yii\base\Event;
use yii\base\Module;
use Exception;

class CachepurgeModule extends Module
{
    public static $instance;

    public function __construct($id, $parent = null, array $config = [])
    {
        Craft::setAlias('@modules/cachepurge', $this->getBasePath());
        $this->controllerNamespace = 'modules\cachepurge\controllers';

        // Set this as the global instance of this module class
        static::setInstance($this);

        parent::__construct($id, $parent, $config);
    }

    public function init()
    {
        parent::init();
        self::$instance = $this;

        Event::on(
            Entry::class, 
            Element::EVENT_BEFORE_SAVE,
            function(ModelEvent $e)
            {
                $entry = $e->sender;
                if (ElementHelper::isDraftOrRevision($entry)) {
                    return;
                }
                $this->purgeFromCache([$entry->getUrl()]);
            }
        );

        Event::on(
            Tag::class,
            Element::EVENT_BEFORE_SAVE,
            function(ModelEvent $e)
            {
                $tag = $e->sender;
                if (ElementHelper::isDraftOrRevision($tag)) {
                    return;
                }
                $tagUrl = App::parseEnv('@web') . "/glossary/" . rawurlencode($tag->title);
                $tagUrlJson = $tagUrl . "/json";
                $this->purgeFromCache([$tagUrl, $tagUrlJson]);
            }
        );
    }

    private function purgeFromCache($urlsToPurge)
    {
        if(!count($urlsToPurge))
        {
            return;
        }

        // Purge from nginx' fastcgi cache
        foreach($urlsToPurge as $urlToPurge)
        {
            @file_get_contents(
                'https://proxy/purge' . parse_url($urlToPurge, PHP_URL_PATH),
                false,
                stream_context_create([
                    "ssl"=>["verify_peer"=>false, "verify_peer_name"=>false],
                    "http" => [
                        "method" => "GET",
                        "header" => "Host: allaboutberlin.com\r\n",
                    ]
                ])
            );
        }

        // Purge from cloudflare cache
        if(App::parseEnv('$CLOUDFLARE_ZONE') && App::parseEnv('$CLOUDFLARE_API_KEY'))
        {
            @file_get_contents(
                '<a href="https://api.cloudflare.com/client/v4/zones/" class="redactor-autoparser-object">https://api.cloudflare.com/cli...</a>' . App::parseEnv('$CLOUDFLARE_ZONE') . '/purge_cache',
                false,
                stream_context_create([
                    "http" => [
                        "method" => "POST",
                        "header" => implode("\r\n", [
                            'Authorization: Bearer ' . App::parseEnv('$CLOUDFLARE_API_KEY'),
                            'Content-Type: application/json',
                            'Accept: application/json',
                        ]) . "\r\n",
                        "content" => json_encode(['files' => $urlsToPurge]),
                    ]
                ])
            );
        }
    }
}
```

What about related pages? If a page's title changes, it will also change on the other pages where it appears. If a new page is added, the index page should be updated to show it. This is where cache invalidation gets hairy. Since I only cache pages for 24 hours, I decided to ignore the issue and not overcomplicate things.

### Clearing the Cloudflare cache

I just make a request to the [Cloudflare API](https://api.cloudflare.com/#zone-purge-files-by-url). Easy peasy.

### Clearing the nginx cache

By default, nginx does not allow you to selectively purge its cache. [It's a pro feature](https://www.nginx.com/faq/does-nginx-plus-support-cache-invalidationcache-purge/). There are two alternative ways to go at it:

1. Figure out [how cache files are named](https://devdocs.io/nginx/http/ngx_http_proxy_module#proxy_cache_path), and delete the right ones
2. Recompile nginx to with the third-party [ngx_cache_purge module](https://github.com/nginx-modules/ngx_cache_purge), and configure it properly

Option 1 is easy, but it can't be done in nginx alone. You need a bit of code outside of nginx to find and delete the cached pages. This would mean that the reverse proxy - the gateway to my website - would be nginx plus a bit of *something else*. Some sort of tiny web server would have to exist somewhere to handle cache purging.

I wanted this to be 100% handled by nginx, so I wasted many days getting option 2 to work. It invoked the exhaustive knowledge and use of English and Canadian French expletives. My bumpy journey led to a [documentation update](https://github.com/nginxinc/docker-nginx/issues/511) and a smoother road for future travellers.

Long story short, I now have this nginx config:

```
location ~ /purge(/.*) {
    # Allow other docker machines only
    allow 172.16.0.0/12;
    deny all;
    fastcgi_cache_purge craftcache "$scheme$request_method$1?q=$arg_q&limit=$arg_limit";
}
```

When I call `allaboutberlin.com/purge/url/to/page`, the page at `allaboutberlin.com/url/to/page` gets purged from the nginx cache. The cache-purging URL is only accessible internally.

## Conclusion

Changes like this one don't seem like much, but they eliminate small interruptions that distract me from my work.

