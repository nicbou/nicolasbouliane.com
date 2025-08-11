---
title: Improving my resignation letter generator
description: A series of small improvements to my resignation letter generator
date_created: 2025-08-10
categories: allaboutberlin
---
Two years ago, I have a released a [resignation letter generator](https://allaboutberlin.com/docs/resignation-letter). There are a few rules and good practices around how these letters should be written, formatted and delivered. This tool makes helps immigrants write a compliant resignation letter.

With help from employment lawyer Andreas Martin, I have made a few improvements to the letter generator.
## Better user experience

Users can fill in information and improve their resignation letter. Some of this information is legally required, so if it's missing, the resignation could be dismissed. For example, the employer's name and address are required.

Instead of leaving spaces blank, I have added placeholders to show that these fields are required and missing. I have updated the style of the placeholders to highlight that. I have also applied this to other letter generators.

![](/images/letter-generator-missing-fields.png)

I have improved the form with better explanations. I tell people how to write their address (it's not obvious to immigrants).

![](/images/letter-generator-address-explanation.png)

You can request a few documents with your resignation letter. I have clarified what each document means, and added *Recommended* markers on documents that you should always ask for. Sensible defaults help people make good decisions.

![](/images/letter-generator-docs-explanation.png)

Ideally, you should always send your resignation letter in German. If you look at the print preview in English, it recommends sending the letter in German.

![](/images/letter-generator-language.png)
## Better content

I have tweaked the text of the resignation letter template. It avoids ambiguous situations, like when the specified resignation date is before the end of the notice period. The new letter requests to resign at the given date *or at the earliest date possible*.

At Andreas' recommendation, I added a preliminary resignation notice to the list of documents you can request with your resignation. This can help your job search, and you are legally entitled to it.

There used to be a guide for writing and sending a resignation letter, and a separate page for the resignation letter generator. I have merged those pages. Keeping the instructions on a separate page makes people far less likely to read them.