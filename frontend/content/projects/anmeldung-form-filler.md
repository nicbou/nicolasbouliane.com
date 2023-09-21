---
title: Anmeldung form filler
description: A tool to help you fill the Anmeldung form.
date_created: 2023-09-19
project_url: https://allaboutberlin.com/docs/anmeldun
---

When you move in Berlin, you must [register your address](https://allaboutberlin.com/guides/anmeldung-in-english-berlin). This involves filling a paper form and delivering it in person - by appointment only - to the Bürgeramt. This is called the *Anmeldung*.

The *Anmeldung* form sucks. It sucked 8 years ago and it sucks now. It's ambiguous and confusing and I hate it, so I made a better one.

**[You can try it here.](https://allaboutberlin.com/docs/anmeldung)**

![Anmeldung form filler screenshot](/images/anmeldung-form-filler.png "It's actually digital!")

It's an actual web form, not a PDF. It works on your phone. It supports autofill, numeric keyboards, field validation, autocomplete, keyboard shortcuts, accessibility tools, etc.

I designed it to [feel more like a conversation](https://service-manual.nhs.uk/content/how-to-write-good-questions-for-forms/think-of-the-form-as-a-conversation), and less like being interrogated by a blunt bureaucrat. The form adapts to your answers and gives helpful instructions. The web is a great medium. We can do more than put a paper sheet on the internet.

![Anmeldung web form](/images/anmeldung-form-part1.png)

I added a dedicated step for ["c/o" addresses](https://allaboutberlin.com/guides/addressing-a-letter-in-germany#if-the-name-is-not-on-the-mailbox). German apartments don't have apartment numbers. If your name is not on your mailbox, postal workers can't deliver your mail. If you can't put your name on your mailbox, you must add "c/o" to your address. This is officially allowed, but it's covered neither by the official form, nor by the official instructions.

![Anmeldung form filler with instructions](/images/anmeldung-instructions-co.png "Using words to explain stuff. Revolutionary!")

The Bürgeramt also wants to know that you live on the second floor on the right. That's not clearly stated on the form (it's the "Zusätze" in "Straße, Hausnummer, Zusätze"). People leave that out, so they get asked (in German) during their appointment.

![The "building details" form field](/images/anmeldung-building-details.png)

At the end, you can download the form. You also get a few options like booking an appointment or hiring help.

![Last step of the Anmeldung form filler](/images/anmeldung-last-step.png)

The form can only fit two people. If you register your whole family, you must fill the same form multiple times. This tool handles it for you.

![Option to download multiple forms](/images/anmeldung-multiple-form.png)

These are small details that make a big difference for immigrants registering their address for the first time.

I also made a few small quality of life improvement: using the browser's language to suggest the user's country, focusing on the right fields when moving between form stages, and a few other niceties. It's subtle, but it adds up to a nice user experience.

## Privacy

Everything happens in your browser. Your personal information never leaves your computer. 

## How it's made

It's a simple VueJS component, like [all the other tools](https://allaboutberlin.com/tools) on All About Berlin.

I use [PDFLib](https://pdf-lib.js.org/) to fill the form in the browser. While the user is filling the form, I download the empty PDF form and the JS library in the background. When they click "save form", it happens instantly. It feels unnaturally snappy.

### Culture sniffing

I use `navigator.languages` to get a list of supported languages. For example, `en-CA`, `fr-CA`, `de-DE`. This gives me a list of countries the user *might* have lived in. I suggest those countries at the top of the country list.

![List of countries with suggested countries](/images/anmeldung-country-picker.png)

This is a technique I first used with the [currency tooltips](/blog/currency-tooltips). It lets you guess a user's culture when the cost of getting it wrong is low.

## What's next?

I'd like to digitalize more forms. The [tax ID request form](https://allaboutberlin.com/docs/010250-antrag-auf-vergabe-einer-steuerlichen-id) is a solid contender, as the original design is offensively bad. The [Abmeldung](https://allaboutberlin.com/docs/abmeldung) form would also be useful.

### Faxes and snail mail

If you don't have a printer, I could mail the form to you. It costs 0.85€ to mail a letter through the LetterXPress API. You could get the filled form in a few days, then bring it to your appointment.

I could digitalize other forms, and fax them through the Simple Fax API. It costs 0.07€ to fax a page. This would let you complete some bureaucratic tasks "fully digitally" a decade before the government gets there.

Anachronistic problems demand anachronistic solutions!

### Go fully digital

Or why not skip paper entirely? During COVID, we filled information online, and showed a QR code at the test centre. Why can't the Bürgeramt have that? Even with in-person appointments, a QR code or a short URL would make paper forms entirely unnecessary.

*This story made the front page of Hacker News. You should [read the comments](https://news.ycombinator.com/item?id=37566992) there.*