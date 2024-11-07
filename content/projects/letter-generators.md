---
title: Letter generators
description: Tools to generate letters in German and in English
date_created: 2024-09-15
project_url: https://allaboutberlin.com/tools
---

Many bureaucratic processes require writing a free-form letter, printing it, signing it, and mailing it to someone.

It's a tedious process even for native Berliners, but it's especially dreadful for recent immigrants who don't speak German and don't understand the system well. Although these letters have no specific format, they are sometimes legally required to include certain information. They also need to have a certain tone to be taken seriously.

I created a simple tool to generate letters for various bureaucratic process. Readers can just fill in the blanks and get a letter that's ready to send. The letters are in the standard [DIN 5008](https://en.wikipedia.org/wiki/DIN_5008) format, and can be viewed in German and in English. The website tells them exactly how to send a letter and where to send it.

![](/images/letter-generator-0.png "A letter generator in context")

![](/images/letter-generator-1.png "The letter template with the blanks left to fill")

![](/images/letter-generator-2.png "Filling the blanks")

![](/images/letter-generator-3.png "The letter changes according to the user's situation. Helpful context is provided.")

![](/images/letter-generator-4.png "The output is a printable letter in the standard German format.")

I hope to make letter-writing a mere formality instead of a stumbling block. This should save immigrants a lot of stress, and make it more likely for them to enforce their rights.

So far, I have built letter generators for [resignation letters](https://allaboutberlin.com/docs/resignation-letter), [apartment deposit recovery](https://allaboutberlin.com/docs/deposit-return), [notifying the immigration office of a job change](https://allaboutberlin.com/docs/auslanderbehorde-job-change), and a few obscure bureaucratic tasks.

## How it's made

It's a simple VueJS component, like [all the other tools](https://allaboutberlin.com/tools) on All About Berlin. I built a generic letter generator, and extend it for each type of letter. The generic component and the utility functions make it easier and easier to create new letter generators.

I built my own HTML-based [DIN 5008](https://en.wikipedia.org/wiki/DIN_5008) letter template with the right margins, sections and typography. Getting it to look exactly right in the browser and as a printed PDF was not easy. The margins are still wrong in Safari, but that's out of my hands.