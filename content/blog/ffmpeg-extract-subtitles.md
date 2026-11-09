---
title: How to extract subtitles with ffmpeg
description: This is how you extract .srt and .vtt subtitles from a video with ffmpeg.
date_created: 2021-08-23
---

My goal was to extract .srt and .vtt subtitles from a video file with embedded subtitles. This is how I achieve it.

### Finding the subtitle tracks

You can directly refer to subtitle streams with ffmpeg's [`-map`](https://trac.ffmpeg.org/wiki/Map). For example, this is how you would find the English subtitles:

```bash
ffmpeg -i input.mkv -map "0:m:language:eng" -map "-0:v" -map "-0:a" output.srt
```

This command uses `-map` to select all English language streams (`eng`), then filters out the audio and video streams, then writes the subtitles stream to a .srt file. You could also write it to a .vtt or .ass file if you want a different type of subtitles.

However, this fails if you have multiple tracks with the same language. ffmpeg will try to fit multiple English subtitle streams in the same .srt file and fail. You will get an error like "SRT supports only a single subtitles stream" or "Exactly one WebVTT stream is needed".

As far as I know, there is no way to select only the first subtitle track of each language. You must use [`ffprobe`](https://ffmpeg.org/ffprobe.html) to find which subtitles stream is where, then extract the streams you want one by one. Here's how you list the subtitle streams:

```bash
ffprobe -v error -of json input.mkv -of json -show_entries "stream=index:stream_tags=language" -select_streams s
```

This command inspects the streams in input.mkv, but only shows the subtitle streams. It returns the kust as JSON. This is useful if you must parse the output.

```json
{
    "programs": [

    ],
    "streams": [
        {
            "index": 2,
            "tags": {
                "language": "eng"
            }
        },
        {
            "index": 3,
            "tags": {
                "language": "eng"
            }
        },
        {
            "index": 4,
            "tags": {
                "language": "ger"
            }
        },
        {
            "index": 5,
            "tags": {
                "language": "ger"
            }
        }
    ]
}
```

Here, you can see that we have 4 subtitle streams: 2 in English and 2 in German. We can extract them one by one by using their index. I only extract the first track for each language:

```bash
ffmpeg -i input.mkv -map "0:2" output.eng.srt
ffmpeg -i input.mkv -map "0:4" output.ger.srt
```

You can combine that into a single command:[^0]

```bash
ffmpeg -i input.mkv -map "0:2" output.eng.srt -map "0:4" output.ger.srt
```

In my case, I need both .srt and .vtt subtitles, so the command is a bit longer:

```bash
ffmpeg -i input.mkv \
    -map "0:2" output.eng.srt \
    -map "0:2" output.eng.vtt \
    -map "0:4" output.ger.srt \
    -map "0:4" output.ger.vtt
```

## Image-based subtitles

The method above won't always work, because some subtitles are image-based, and not text-based[^1]. They can't be converted to .srt or .vtt.

I did not find a way to filter out image-based subtitles with ffprobe. I saw that image-based subtitle streams have width and height attributes, while text-based ones don't.

```json
{
    "streams": [
        // This subtitle stream has width/height. It's image-based.
        {
            "index": 5,
            "codec_name": "dvd_subtitle",
            "codec_type": "subtitle",
            "width": 720,
            "height": 480,
            "tags": {
                "language": "eng"
            }
        },
        // This subtitle stream has no width/height. It's text-based.
        {
            "index": 8,
            "codec_name": "subrip",
            "codec_type": "subtitle",
            "tags": {
                "language": "eng"
            }
        },
    ]
}
```

However, that's not always true. Some image-based subtitle streams (like `hdmv_pgs_subtitle`) don't have a width or height. In the end, your only option is to look for specific codecs that you *know* are text-based.

You can see my current implementation [here](https://github.com/nicbou/homeserver/blob/master/videoprocessing/src/jobs.py#L120), in the `extract_subtitles` function.

[^0]: [trac.ffmpeg.org](http://trac.ffmpeg.org/wiki/Creating%20multiple%20outputs)
[^1]: [stackoverflow.com](https://stackoverflow.com/questions/58808907/is-it-possible-to-determine-if-a-subtitle-track-is-imaged-based-or-text-based-wi)