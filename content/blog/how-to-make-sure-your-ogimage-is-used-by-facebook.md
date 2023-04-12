---
title: How to make sure your og:image is used by Facebook
description: How EXIF data can prevent Facebook from using your thumbnail images.
date_created: 2016-03-18
---

You can define custom meta tags on your website to decide it will appear when shared on Facebook. One of them is the og:image tag.

Unfortunately, it does not work reliably, and even their [Open Graph debugger](https://developers.facebook.com/tools/debug/) won't help you. For instance, I got the following message:

```
og:image should be larger: Provided og:image is not big enough. Please use an image that's at least 200x200 and preferably 1500x1500. (Maximum image size is 5MB.) Image 'url from image, size: 300x443px 97kb' will be used instead.
```

My image fit all the criteria and even showed in the og:image preview, yet Facebook refused to use it. **It turns out that EXIF data was the culprit.** Stripping the image of EXIF data and reuploading it solved the problem. This odd solution is supported by members of various communities.

If you are using WordPress, you can use plugins to set Facebook meta tags and automatically strip images of EXIF data, but there is no plugin that lets you strip EXIF data only for featured images.

