---
title: File names, unicode normalization problems, and how to fix them
description: There are multiple ways to represent the same unicode character. This can cause problems. Here's how I fixed it.
date_created: 2023-07-14
---

There are [many ways to represent the same accented character](https://en.wikipedia.org/wiki/Unicode_equivalence) in Unicode.

For example, `Ü` can be represented as `Ü` (U+00DC)  or as `U + umlaut` (U+0055 plus U+0308).

They look like the same character, but when compared, they are not equivalent:

```bash
>>> '\u00DC'
'Ü'
>>> '\u0055\u0308'
'Ü'
>>> '\u00DC' == '\u0055\u0308'
False
```

To avoid problems, we pick one way of representing accented characters, and we stick to it. This is called *normalization*. There are two normalization forms: NFC, which prefers composed characters (like U+00DC), and NFD, which prefers decomposed characters (like U+0055 plus U+0308).

Different software and filesystems use different normalization forms. This can lead to problems. For example, **I used Syncthing to backup files, and it converted NFC filenames to NFD**. This broke All About Berlin, who looked for pages like `./glossary/Bürgergeld.md` that no longer existed. The `ü` in `Bürgergeld.md` was represented differently in the code, and in the filename.

I wrote a small script to fix this. It's at the end of this post.

## Python and Unicode normalization

In Python, the `unicodedata` package handles normalization. You can use `unicodedata.normalize` to convert between normalization forms.

```
>>> from unicodedata import normalize
>>> '\u0055\u0308' == normalize('NFD', '\u00DC')
True
>>> '\u00DC' == normalize('NFC', '\u0055\u0308')
True
```

After Syncthing borked my files with Unicode characters in them, I wrote this short script to fix it. It converts the file names back to NFD.

```python
#!/usr/bin/env python3
from pathlib import Path
from unicodedata import normalize

for file in list_of_files:
    current_form = file
    normalized_form = normalize('NFC', file)
    if current_form != normalized_form:
        Path(file).rename(normalized_form)
```

## Syncthing and unicode normalization

By default, Syncthing automatically fixes unicode normalization errors. In my case, it kept renaming the files to the "wrong" format used by All About Berlin's files. You can change the [`autoNormalize` setting](https://docs.syncthing.net/advanced/folder-autonormalize.html) to `false` in your [`config.xml`](https://docs.syncthing.net/users/config.html), and that will disable that feature.