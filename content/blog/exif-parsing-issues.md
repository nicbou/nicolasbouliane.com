---
title: Weird things you'll find when reading EXIF data
description: I wrote code that extracts EXIF data from photographs. Here are some of the weird things you can expect.
date_created: 2020-12-10
---

I wrote [python code](https://github.com/nicbou/timeline/blob/24ce4ad64f1de83e19978876870dbcb451312093/backend/source/backup/utils/files.py#L316) that uses Pillow to extract EXIF data from thousands of photographs for [my timeline thing](/projects/timeline). It processes tens of thousands of personal photos. These are some of the oddities I encountered:

- **Null bytes**  
    The ImageDescription, Make, Model and various Date/TimeStamp fields can contain null bytes. It's a very common problem, and it can break things down the pipeline. You must use `.replace('\x00', '').strip()` on most fields, including the title and description fields.
- **Invalid date formats**  
    The default EXIF date format is `'%Y:%m:%d %H:%M:%S'`. Some photos used `'%Y-%m-%d %H:%M:%S'` or even `'%Y-%m-%dT%H:%M:%S+%Z'` instead.
- **Missing GPS attributes**  
    One photo had a GPSDateStamp, but no GPSTimeStamp. One had a GPSLongitude but no GPSLongitudeRef.
- **Conflicting attributes**  
    There are multiple ways to store the title and description, and different software does it differently. Is the description in ImageDescription, XPComment, or Description? It depends on what software created or modified the image.
- **Useless data**  
    Olympus cameras will caption every picture with "OLYMPUS DIGITAL CAMERA". Not just in the Make and Model fields, but also in the ImageDescription field.

That's all for now. It seems to process tens of thousand of photos without issues.

