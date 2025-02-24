---
title: Feasibility study: Welcome Center Berlin
description: A report about building a new website for the Welcome Center, an official website to welcome immigrants to Berlin.
date_created: 2025-02-01
---

This is a feasibility study for the new website of the [Welcome Center Berlin](https://www.berlin.de/willkommenszentrum/). This a counselling centre for immigrants run by the [Senate for Participation, Integration and Migration](https://www.berlin.de/lb/intmig/). My report was commissioned by [Minor](https://minor-kontor.de/).

The following assessment and recommendations are based on my experience running [All About Berlin](https://allaboutberlin.com) since 2017, and my 15 years of experience as a web developer.

The sections of the report mirror those of [the requirements document](/files/minor-requirements-2025-01-21.pdf), which you should read first.

{% include "blocks/_tableOfContents.html" %}

## Foreword

### Priorities and assumptions

I have prioritised the impact and longevity of this project, given an initial budget of around 50,000€. I have assumed that there will be a smaller yearly budget for maintenance and further development, and that this budget will be subject to political winds. I chose to favour resilience and low maintenance costs wherever possible.

A higher budget would not significantly affect my recommendations.

### Simple is cheap

Add as little complexity as you need to get the job done. Software is complex, and complexity is expensive. This will be a common theme in my report.

A text-based website is cheap to build, maintain and adapt. Once it's built, anyone can make changes to its content. Such websites can run forever with minimal maintenance. The only downside is the user experience; text takes more effort to read and understand.

Software is the opposite. Good software can save time and offer a magical user experience. However, it's much more expensive to build, adapt and maintain. The work must be done by skilled professionals. You must allot time and money to server upkeep, software updates, and so on. Software is a commitment, and its upkeep is a tax.

![Information is cheap and effective](/images/illustrations/information-cheap-effective.png "Text-based information is cheap and effective")

### Bet on text

More often than not, text is a much better choice than software.

Text is as flexible as it gets. It can be cited, linked to, emailed and printed. It can be found through Google, archived, subscribed to, saved for online reading, translated, summarised by AI and read by accessibility tools. It can automatically be turned into PDFs, newsletters, flyers e-books and podcasts.

Text is also platform-agnostic. It's easy to move around, and is far more likely to survive across multiple website redesigns. It does not rot and fall apart like software.

It might be tempting to build fancy features, but the magic is often in doing simple things really well.

### Castles on quicksand

You can't build a rigid digital layer on top of an unpredictable analog bureaucracy.

German bureaucracy is too arbitrary and inconsistent to describe with code. Each district, each office and each bureaucrat interprets the law differently. They make arbitrary decisions based on undocumented policies that change without warning. This is not a stable foundation to build rigid software upon.

### Sheds and skyscrapers

Complex projects require specialised labour. Specialised labour is more expensive and harder to find.

You can easily find freelancers to work on a WordPress website. It might be harder to find maintainers for a fancier technology stack. It's even harder if you can't pay market rates, or if you only need a developer for a few hours every now and then. Maintaining complex software can become a human resources problem.

[Choose boring technology](https://mcfunley.com/choose-boring-technology), especially if you don't have an in-house development team to maintain it.

## 1. Intelligent search

### 1. Description

> ‘Intelligent’ search field with filter options to personalise results (e.g. by nationality, residence status, language, etc.) as well as automatic completion of the search query and correction of spelling errors to improve accuracy

!["Intelligent search box"](/images/illustrations/padi-intelligent-search.jpg "CityLab's search box prototype")

### 2. Technical requirements

#### Simple search

Most CMSes come with lexical search. It searches for words in documents. This is what most websites use.

Lexical search is "fuzzy". It matches nearby words, like plural forms (cook → cooks), similar stems (root → rooted), and words a few letters apart (flaw → flow).

This is the default; it comes as a feature of most CMSes, so it does not require extra effort to implement.

Example lexical searches: [rbb24.de](https://www.rbb24.de/suche/#searchform_q__landesamt,,20f,,C3,,BCr,,20einwanderung___start__0___fromSearchbox), [settle-in-berlin.com](https://www.settle-in-berlin.com/?s=anmeldung)

#### Intelligent search

Semantic search is a little smarter. It matches meaning instead of words. For example, people might search for "visa" when they mean "residence permit". Semantic search returns results that are conceptually similar.

Good semantic search is much harder to implement.

#### Filters

Users can filter search results by various criteria. For example, most online shops let you filter products by price, category, colour and size.

Your pages have metadata: tags, categories, extra fields and other taxonomies. You can filter search results by that metadata. This is a standard feature in most CMS.

The CityLab prototypes showed a search that returns different *kinds* of results. For example, searching for "meld" can return "Meldebescheinigung" (glossary term), "Anmeldung" (guide), "Anmeldung" (tag), "Meldebescheinigung" (document template), etc.

#### Global search

You mentioned that your search should return results from other websites. Searching for "Anmeldung" should return the address registration page from service.berlin.de.

### 3. Artificial intelligence

Artificial intelligence builds upon good search. Good search builds upon good content.

Usually, AI can't fit your entire website into its brain, so it searches your website and generates a response from the first few results. This is called retrieval-augmented generation (RAG).

If you build a chatbot, AI search and other AI tools, you will likely use RAG. RAG only works well if your search works well. In other words, to build a good AI, you must first build a good search.

### 4. Feasibility assessment

#### Search

Search is a feature. *Good* search is a project. Given your budget, aim for "good enough".

Lexical search is good enough, and it's very easy to implement. It meets most people's expectations, especially on a small website with a few hundred pages. It's also easy to suggest different types of results in the search bar (categories, tags and pages), like in the CityLab prototypes.

Semantic search is possible, but it's more work. There are off-the-shelf solutions for this, but they must be implemented, then customised and adjusted to your needs. This can take significant development time.

[Algolia](https://www.algolia.com/) and [ElasticSearch](https://www.elastic.co/enterprise-search/) are two of the biggest providers. You feed them your documents, and they give you a search box. These solutions are deployed by large organisations to search across many departments and websites. These solutions are overkill for your needs.

[Google Programmable Search Engine](https://programmablesearchengine.google.com/about/) could also work. It's basically search results from Google, but limited to your website. It's halfway between basic lexical search and the fully customisable experience of other off-the-shelf solutions.

Global search across multiple websites is much more difficult. You would need to crawl all those websites yourself, filter out useless pages, evade anti-bot measures, and figure out how to rank those results. Then you would definitely need tools like Algolia or ElasticSearch. You would effectively build your own little search engine. This is well beyond your budget.

Search can always be improved later. Implement basic lexical search now, gather usage data, and improve it later as needed. Semantic search might stretch your budget. AI search would definitely exceed it.

#### Filtering

Filtering is easy to implement. Most CMSs provide utilities that make it possible. Returning different *kinds* of results (categories, tags, guides, articles, document templates) is also easy to implement.

To get good filters, you need good metadata. Filters only work when every page is correctly tagged, categorised, and all the fields are correctly filled in. The search filters of an online store only work if the metadata for every product is meticulously filled in. You can only filter clothes by colour because someone added colour data to every product.

![Amazon product filters](/images/illustrations/padi-product-filters.png "Product filters require detailed product data")

In your case, this means carefully considering how you organise, categorise and tag your content. Consider how much effort this could mean for your editors.

For example, to filter information by nationality, you must manually tag every page with the nationalities it applies to. If this information changes, all pages must be re-tagged without making any errors. This happens often! The United Kingdom left the EU. Romania joined the Schengen Area. Montenegro signed a pension agreement with Germany. Someone must update that data everywhere, every time, forever. Will enough people use the search filters to make this worthwhile?

I suggest filtering by simple taxonomies like category, responsible *Amt*, language and tags. You likely need to create those taxonomies to organise the content on your website anyway.

### 5. Risks and challenges

Semantic search is harder to get right. It might not work well when mixing multilingual content with specialised German terms. A search engine might understand the proximity of the words "king" and "prince", but it might not understand the relationship between "Anmeldung", "Meldebescheinigung" and "Meldebestätigung" for example, especially not in an English-language document. Likewise, if someone searches for "LEA", it might not return results for "Landesamt für Einwanderung" unless both terms are in the same document.

Content can only be searched for if it's indexed. All the text in an article is searchable. The title, description, tags and categories are usually searchable. The text inside interactive tools might not be searchable - neither by our internal search nor by search engines like Google. In that sense, interactive tools can make your advice harder to discover.

It's possible that nobody really uses your search feature. All About Berlin gets 7 searches for every 1,000 visits. If most of your visitors come directly to the right page from Google, search engine optimisation is a better investment.

## 2. Interactive guides

### 1. Description

> Clickable, interactive and customisable (e.g. according to the languages spoken, residence status, length of stay, etc.) step-by-step instructions that guide users through bureaucratic processes in a simple and understandable way.

This feature is about creating interactive guides to navigate users through bureaucratic processes. You ask them questions, and their answers lead them to a recommendation. This is an improvement over simple text instructions.

![Interactive questionnaire](/images/illustrations/padi-interactive-guide.png)

Let's call those tools "interactive guides".

### 2. Technical requirements

You can create interactive guides one by one, as bespoke software. This is the approach I take.

Your content editors might want to build tools themselves. They could create and update interactive guides without hiring expensive software developers every time. A tool could help them create flowcharts, and automatically turn those flowcharts into an interactive guide for the website.

For this, they would need *no-code tools*.

### 3. Artificial intelligence

I see no applicable use of AI here. These tools navigate users through rigidly-defined processes. There should be no uncertainty, and no room for an AI to guess what to do. AI advice is error-prone, difficult to test, and likely to give incorrect advice the appearance of trustworthiness.

### 4. Feasibility assessment

Each interactive guide is its own mini project with its own requirements.

I takes me two to six weeks to build a single interactive guide. The first ones take longer to build, because developers must build the groundwork that is reused for each tool afterwards.

It might take longer in your case, because the work is defined by one team and done by another. It also takes time to understand and define the logic behind each tool. If that knowledge comes from a third team, it adds more delays.

There might be off-the-shelf solutions to create interactive guides without coding. If these tools exist, they might require significant development time to adapt to your needs.

There is [Floma](https://floma.io/), a tool built for the calculator on [Mietencheck.de](https://mietencheck.de/), but it's not mature software yet. The closest mature solution is [VisiRule](https://www.visirule.co.uk/solutions/decision-tree-flowcharts), but it might not do exactly what you need. There is also a [white paper](https://vis4good.github.io/papers/2023/zhou.pdf) about a similar tool, but I found no immediately usable solutions.

In my opinion, this feature is not achievable within your budget. Bespoke interactive guides are expensive to build. A tool that lets you build your own interactive guides is several times more expensive, and it might still fail at its task.

### 5. Risks and challenges

Offering those interactive guides in multiple languages adds a layer of complexity. Every question, answer and verdict must be translated to multiple languages. If you choose the no-code route, it will be hard to do this through an intuitive user interface. If you use off-the-shelf solutions, they might not support multiple languages at all.

Interactive guides need regular maintenance. Bureaucratic processes change often and without warning. A bureaucratic change might require a complete overhaul of your tools. There is also a lot of variance in German bureaucracy. It might not be possible to describe processes as a simple flowchart with a well-defined outcome. See ["castles on quicksand"](#castles-on-quicksand) above.

Search engines only index what they can see. They do not see the useful information buried multiple steps deep into an interactive guide. Interactive guides make information less discoverable for people using Google, ChatGPT or your own search. You might need to maintain two versions of your advice: a text version, and an interactive guide.

## 3. Interactive checklists

### 1. Description

> Clickable, interactive and customisable (e.g. according to the languages spoken, residence status, length of stay, etc.) step-by-step checklists to support users in preparing documents to be submitted for applications or in checking the requirements.

This feature is about offering smart lists of documents. There are two ways to imagine this:

- **Make the list smart**  
    The user enters information about themself, and they get a personalised list of instructions or documents to prepare, based on their situation.
- **Make the elements more useful**  
    A regular list, but the list elements are more than just text. For example, they can have a "?" button that explains what the document is and where to find it. The list could show previews of the document or link to a PDF template. The editors can create those rich list items and reuse them in multiple lists.

![Rich list elements](/images/illustrations/padi-rich-list-elements.png "Rich list elements")

### 2. Technical requirements

The requirements for an interactive checklist are the same as for interactive guides. Each interactive checklist is its own mini project. You must figure out all the possible checklist combinations and build the logic to display them. Then you are no longer writing text, but programming rules. You are writing software. Once again, you can pay software developers to do it every time, or pay a much higher price to let them build software to edit the list yourselves.

Rich list elements are much easier to make. They are just a nice way to present the information. You create documents using the CMS, and you insert a list of those documents in your posts. We can present these documents however we want: in a collapsible panel, with a little information bubble, etc.

### 3. Artificial intelligence

Artificial intelligence can be used to quickly add a lot of information about a long list of documents. However, AI generated content tends to be too vague to be useful, and too inaccurate to be trustworthy.

### 4. Feasibility assessment

Interactive checklists are not achievable within your budget. They work exactly like interactive guides, and they are unachievable for the same reasons.

Rich list elements are possible, and very easy to implement. This feature is well within your budget.

### 5. Risks and challenges

Requirements are not fixed in stone. They vary by office, department and case worker. They change without warning, and are rarely well-documented. The official information on Berlin.de is often incorrect. Gathering correct information is a lot more work than choosing how to present the information.

See ["castles on quicksand"](#castles-on-quicksand).

## 4. Automatic translations

### 1. Description

> Automatic translation of content and switching between different languages to ensure the multilingualism of all content in different formats (text content, infographics, explanatory videos)

This feature is about automatically translating the content, interface and tools on the website.

### 2. Technical requirements

You must translate everything. Not just the page body, but also the title, the short description, the categories, the tags, and every other bit of content on the website.

Besides the content, you must also translate the user interface: every menu, form, tool and button. This is a separate process with its own pitfalls, but it's easy to train people to do it. The tools are very intuitive.

If you use external software (for example, a no-code tool to create interactive guides), those tools must also support multilingual content.

Translation is a process. Each change in the original content must lead to a corresponding change in the translations. There should be a mechanism to mark translations as out of sync.

### 3. Artificial intelligence

This feature is about using artificial intelligence to translate the content. It necessarily involves the use of artificial intelligence.

### 4. Feasibility assessment

I have experimented with automatic AI translations for All About Berlin. The goal was to offer the entire website in multiple languages with minimal extra labour. I had mixed results.

On one hand, translating the whole website was incredibly cheap: around 15€ per language. Updating translations cost a fraction of a penny.

On the other hand, the translations had many errors. Some were silly mistranslations, but others were seriously misleading.

I recommend to use AI translations *in support* of human editors. AI can suggest translations, and humans can refine the final text.

There are many mature, established tools to do this. Many of them integrate directly into WordPress, and with your editors' workflow. [WPML](https://wpml.org/features/) and [Lokalise](https://lokalise.com/solutions/web-localization) are two well-known options.

### 5. Risks and challenges

There are many issues with automated translations:

- Some advice only makes sense in one language. For example, a list of English-speaking lawyers.
- The content gets translated, but not the links. The translation tool can't automatically replace links with their French equivalent.
Some acronyms like "PR" (permanent residence) have no equivalent in other languages.
- Some terms have very specific legal translations. For example, the Berlin immigration office is the Landesamt für Einwanderung. Permanent residence is called Niederlassungserlaubnis. AI uses various translations interchangeably.
- Translations can be longer than the original text and break the website's design.
- Style guides are really hard to apply. AI can be inconsistent about tone, formality, gendering and other stylistic matters.

Some of these problems can be mitigated. Prompt engineering can suggest specific translations. Software post-processing can replace links with their known translation. However, generally speaking, machine translation is not reliable. You either need human oversight, or a very big warning sign above AI-translated content.

Even bad translations can be helpful. French users who get French search results might not find a German website, but they might find the French translations. Translations can multiply the traffic you get. Some of those readers might be happy to read your content in its original language, even if their browser is set in another language.

## 5. Application aid

### 1. Description

> Multilingual completion aids for analogue applications/forms as well as for digital applications/forms hosted on other platforms to enable independent completion of complex bureaucratic processes without access to external advice

This feature is about gathering information from a user in the language of their choice, then completing complex bureaucratic tasks on their behalf, automatically.

### 2. Technical requirements

This solution requires building a layer on top of existing bureaucratic processes. [As highlighted before](#castles-on-quicksand), this implies building rigid software on top of arbitrary, undocumented and capricious bureaucracy.

### 3. Artificial intelligence

I see no applicable use of AI here. This is something that AI agents are designed for. However, the technology is not yet mature enough to implement. AI agents are error-prone, difficult to test, and likely to give incorrect decisions the appearance of trustworthiness.

### 4. Feasibility assessment

Berlin does not offer an API for its digital processes. For the most part, Berlin does not offer digital processes. It's mostly analog processes over email.

For every step of the process, you must create scripts that mimic the actions of a human: clicking around, downloading forms, filling PDFs, sending emails and making payments. This sort of automation - with a [headless browser](https://en.wikipedia.org/wiki/Headless_browser) like Selenium or Playwright - is slow and unreliable. You might also get blocked or rate-limited by the Berlin.de servers.

The response from the bureaucracy is not an instant, predictable, machine-readable message. A human will write a unique letter and mail it to user's home address in 4 to 8 weeks.

Each of the 12 districts handles bureaucracy in its own way, with varying requirements and varying efficiency. You must either adjust your automated solution to the whims of each district, or send all your applications to the single district that does its job well. In my experience, no district will volunteer for this.

The few existing digital processes only work with BundID, which most immigrants can't use, and which your scripts can't work around.

Put simply, Berlin's bureaucracy is actively hostile to automation. In any case, this feature would not be achievable within your budget.

If you can't automate a process, simplify it in increments. Use calculators, interactive guides and message templates to reduce friction at each step. Semi-automation is a lot more achievable.

![Autonomation](/images/illustrations/padi-autonomation.png)

For example, All About Berlin simplfies the [Anmeldung](https://allaboutberlin.com/glossary/Anmeldung) process at every step:

- [A tool](/projects/anmeldung-form-filler) helps users fill the Anmeldung form.
- [Another tool](/projects/appointment-finder) helps them find a Bürgeramt appointment.
- [A guide](https://allaboutberlin.com/guides/anmeldung-in-english-berlin) explains why the Anmeldung is important, how to do it, and how to get the required documents.

![Anmeldung appointment finder](/images/aab-appointment-finder.png "An Anmeldung appointment finder")

### 5. Risks and challenges

See ["castles on quicksand"](#castles-on-quicksand).

## 6. Simple language

### 1. Description

> Automatic translation of content (text content, infographics, explanatory videos) into simple language and switching between complex language and simple language to ensure low-barrier accessibility

This feature is about automatically translating the content to plain language.

### 2. Technical requirements

The requirements, methods and challenges are exactly the same as for [automatic translations](#4-automatic-translations). For the most part, you can treat simple language as just another language.

### 3. Artificial intelligence

Artificial intelligence can aid writers by making suggestions as they type. The quality of the advice varies wildly from valid suggestions to hallucinated corrections, so human judgement is needed.

### 4. Feasibility assessment

Plain language [benefits everyone](https://www.nngroup.com/articles/plain-language-experts/) and should be the default.

AI and non-AI tools can be used to highlight passages that need improvement. It can suggest better ways to write. However, AI cannot be trusted to simplify text without losing important context.

AI tools can aid skilled editors with plain writing, but they can't replace skilled editing work. These tools don't need to be integrated in your CMS; they just need to be available to your editors. I would suggest simply making [Deepl Write](https://www.deepl.com/de/write), [Language Tool](https://languagetool.org/de), [Hemingway](https://hemingwayapp.com/) or [Grammarly](https://www.grammarly.com/) available to your editors, and making plain writing part of your style guide.

![Deepl Write](/images/illustrations/padi-deepl-tones.png "Deepl Write helps you write in plain language.")

### 5. Risks and challenges

See ["automatic translations"](#4-automatic-translations).

## 7. Chatbots

> Recording the questions, profiles (e.g. nationality, residence status, language, etc.) and counselling needs of those seeking advice by questionnaire and by chat or clickbot in order to be able to offer personalised information and referrals or to narrow them down to the specific situation.

See ["interactive guides"](#2-interactive-guides). The work, the challenges and my conclusion are the same.

## 8. Calculators

### 1. Description

> Calculator (e.g. for living costs, financial support, housing benefit, etc.) with personalisation functions using filters to estimate costs or financial support in your own situation.

![All About Berlin tax calculator](/images/illustrations/aab-tax-calculator.png "An income tax calculator on All About Berlin")

### 2. Technical requirements

Building calculators is similar to building [interactive guides](#2-interactive-guides), just easier. Calculators usually follow a simpler logic. They apply clearly-defined formulas instead of an approximate flowchart of a bureaucratic process. In many cases, they just multiply one number by another.

![Trade tax calculation](/images/illustrations/padi-gewerbesteuerrechner.png "The trade tax calculation is basic arithmetic")

Maintaining calculators is much easier. The formulas change on a predictable schedule. For example, most tax calculations change on January 1. The changes are observable, because they are set by law. If you monitor [§32a EStG](https://www.gesetze-im-internet.de/estg/__32a.html), you get an email every time the income tax formula changes.

### 3. Artificial intelligence

I see no applicable use of AI here. Calculators apply clearly-defined formulas. There should be no uncertainty, and no room for an AI to guess what to do. AI advice is error-prone, difficult to test, and likely to give incorrect advice the appearance of trustworthiness.

### 4. Feasibility assessment

Calculators have the same drawbacks as [interactive guides](#2-interactive-guides). You need a developer to build and maintain them. They must be updated when the formulas change. However, due to their simpler logic, you can build them much faster, and they require far less maintenance.

In some cases, these calculators already exist, and it's much easier to link to them. It saves you the trouble of building and maintaining yourself.

You can also licence other people's calculators and embed them on your website. For example, Lexware Office uses a [Smart Rechner](https://www.smart-rechner.de/widget.php) calculator on [this page](https://office.lexware.de/wissenswelt/rechner-checklisten/gewerbesteuerrechner/). Their licencing fee is 15€ to 36€ per month, but their calculators are only in German.

### 5. Risks and challenges

The calculators require regular maintenance to remain accurate.

## 9. Saved content

### 1. Description

> Saved search and favourite services (with and without user account) to quickly retrieve relevant content (including step-by-step instructions and checklists in progress, see [2](#2-interactive-guides) and [3](#3-interactive-checklists))

This feature is about starring important content for easy access, and about remembering user actions and preferences.

!["Save this" button](/images/illustrations/padi-save-feature.png)

### 2. Technical requirements

This information can be saved in the browser's local storage. This information is never transmitted to us. It's a simple, privacy-friendly, GDPR-compliant way of saving user preferences.

If we set the correct "autocomplete" attribute on form fields, we can let the browser autofill form fields. It's very easy to implement, and it saves the user a lot of time.

Some preferences can be inferred from the information given by the user's browser. For example, we get a list of the languages the user speaks. We can use it to set the default language. We can also infer other data, such as their country of origin and their preferred currencies. [I used this technique](/projects/anmeldung-form-filler#culture-sniffing) in my Anmeldung form filler.

![Culture-sniffing form field](/images/anmeldung-country-picker.png "This field uses 'culture sniffing' to suggest the user's country")

Syncing the user's settings across multiple devices is harder. Then you need users accounts, and save their information on your server. This involves sending activation emails, enabling password changes and password recovery, and a host of other small tasks. This needs to be done in a [GDPR-compliant](#4-privacy) way, so users must be able to delete their account, and you must delete unused data after some time.

![Syncing between a smartphone and a laptop](/images/illustrations/padi-sync.png)

This adds a lot of complexity to your project, and the benefit to users is questionable. It might be easier to re-enter the information than to create a user account.

### 3. Artificial intelligence

I see no applicable use of AI here.

### 4. Feasibility assessment

Saving user preferences is easy. Saving recent or starred content is also easy. This should not add significant development time.

### 5. Risks and challenges

The biggest challenge is managing changes.

For example, a user ticks items #1, #4, and #5 in a list. What happens if you rename some items or move them around? How do you know which items to tick when the user visits the website again?

Another example: you save a user's progress through an interactive guide. What happens if the process changes?

## 10. Glossary

### 1. Description

> Glossary function via tooltips to explain complex and important terms without redirecting users to a specific page

This feature is about showing word definitions in a tooltip.

![All About Berlin glossary](/images/glossary.png)

### 2. Technical requirements

I have implemented glossary entries on All About Berlin. They are just another type of content, just like posts, pages and documents. When I link to a glossary entry, the link is automatically replaced by a glossary pop-up. If the user disables JavaScript, the glossary links work as normal links.

This is a beloved feature that gets a lot of use. It helps users without cluttering the text with basic information. It also means that I define the information in one place then use it everywhere. It makes maintenance much easier.

### 3. Artificial intelligence

Artificial intelligence can be used to rapidly create the text for glossary items. However, the information should be clarified and improved upon by humans. AI text tends to be too generic to be useful.

### 4. Feasibility assessment

Implementing glossary tooltips is very easy. It should not meaningfully impact the budget or the development time.

### 5. Risks and challenges

I cannot think of any specific risks or challenges for implementing this feature.

## 11. Extras

These features are not part of the initial requirements, but were brought up during subsequent calls.

### Change monitoring

You might want to use change monitoring tools to watch pages on Berlin.de for changes. If the page changes, you get an email showing what changed. I monitor hundreds of pages like this. It's an essential part of my job. For this, use [changedetection.io](https://changedetection.io).

### Style guide

The website must follow the [Berlin.de style guide](https://styleguide.berlin.de/), and use the elements from their design system. This is a good thing. It saves you a lot of time, because the supplied components already take care of style, functionality, accessibility and mobile friendliness. Best of all, another team handles their maintenance.

Using this design system with your CMS of choice should not be a problem. You must use the base templates as described [here](https://support.berlin.de/designsystem/auftritte/layout-vom-designsystem-per-template-integrieren-1443859.php).

## API access

The websites listed in the proposal do not have a public API. They are not designed to be operated by other machines. Many of those website implement anti-bot measures. They either limit the rate of requests, or block bots outright. It would be difficult for your software to access their data.

As explained in the ["application aid"](#5-application-aid) section, the planned feature is not feasible with the allocated budget.

### Service-Portal

Berlin.de [has an API](https://gitlab.opencode.de/eappointment/zmsdldb), but its not public. Its address is unknown. It might not be accessible to you. This API gives you access to [the central database of all services](https://www.berlin.de/moderne-verwaltung/buergerservice/im-netz/service-portal-berlin/dienstleistungsdatenbank/artikel.976708.php). It would let you get information about those services a little more easily, without having to scrape the service pages.

Accessing this database would allow you to get up-to-date information about government services; a machine-readable version of the service pages on Berlin.de.

Accessing this database would make it easier to monitor those services for changes. Change monitoring can also be done by tools like [changedetection.io](https://changedetection.io).

### Landesamt für Einwanderung

To my knowledge, the LEA offers no public API.

The most important resource the LEA offers is the [VAB](https://allaboutberlin.com/out/vab). This PDF document is a detailed explanation of all their internal procedures.

This document is only available as a PDF. I have pressured them to release it in a more accessible (and machine-readable) format, but I have never received a response.

Having this information in a better format would allow us to link to specific parts of the document, and to watch each section for changes. It would also serve as a reference for the immigration community, a bit like [gesetze-im-internet.de](https://www.gesetze-im-internet.de/).

### Berliner Beratungsnetz für Zugewanderte

They have built an API for their own use. Their website calls this API to know which items to display on the map.

With their permission, you could use this API to get their list of services. It could help you recommend the same services on your website.

Technically speaking, CORS policies might prevent you from using this API. You might need to bypass this by proxying it through your server. It's not hard, but it adds more moving parts to your project. If it does not benefit the user, I would recommend against it.

### Jobsuche-Portal der Bundesagentur für Arbeit

The Bundesagentur für Arbeit has a REST API to search for jobs, but linking to their website directly will offer a better user experience.

### Anerkennungs-Finder von „Anerkennung in Deutschland“

There is no API for this tool. Linking to the tool directly will offer a better user experience.

### Interaktiver Einbürgerungstest des Bundesamt für Migration und Flüchtlinge

There already exist tools and apps that help people practice for the Einbürgerungstest. They all use the official list of questions. Curate a list of those tools instead of building your own.

### Bundesministerium für Arbeit und Soziales

To my knowledge, the BMAS does not offer any public API, or any tools which you could use on your website. However, their calculators use very simple formulas and can trivially be reproduced on your side.

## Additional requirements

### 1. Mobile first

Mobile-first design has been the standard for over a decade. It is expected that the website must adapt to mobile screens, and both designers and developers can be expected to take this into account.

You must use Berlin.de's style guide. The templates and components they provide are already mobile-friendly. This saves you a lot of time.

### 2. Multilingual content

This has been covered in more details in the [automatic translations](#4-automatic-translations) section.

We have mature tooling to build multilingual text-based websites. However, it adds a layer of complexity to any tool that you choose to build.

The hardest part is simply maintaining one version of your content for each language, and keeping those in sync. Tools exist to make this easier, but it cannot be entirely automated.

### 3. Accessibility

A basic level of accessibility can be expected. Full [WCAG compliance](https://www.wcag.com/resource/what-is-wcag/) (AAA) is also feasible, especially if it's part of the requirements from the start. You can demand that the final website to pass WCAG AAA accessibility requirements.

See [this example accessibility test](https://www.accessibilitychecker.org/audit/?website=https%3A%2F%2Fallaboutberlin.com%2Fguides%2Fgerman-health-insurance&flag=ge) for an idea of what accessibility requirements look like.

Making text content accessible is easy. Making graphics, videos and interactive tools accessible is harder. It might add to the cost and complexity of including those things on your website.

You must use Berlin.de's style guide. The templates and components they provide are already accessible. This saves you a lot of time.

The *[Landesbeauftragte für digitale Barrierefreiheit](https://www.berlin.de/lb/digitale-barrierefreiheit/)* and the [ITDZ accessibility team](https://www.itdz-berlin.de/allgemeines/digitale-barrierefreiheit/) can help you implement and test accessibility on your website.

### 4. Privacy

GDPR (DSGVO) is only a concern if you collect data about your users. This can happen if you track your users, or if you collect and store information about them through forms, user accounts or cookies. The easiest way to conform to data protection laws is to not collect any data.

You can still collect anonymous statistics while respecting the GDPR. On All About Berlin, I use [Plausible Analytics](https://plausible.io/). Your statistics lose some precision and granularity, but they give you sufficient insight into your user base.

You can also collect personal data, so long as you collect it with consent, use it for its intended purpose, store it securely and delete it when it's no longer needed.

## Available options

For your needs, I would consider WordPress or Craft CMS.

### WordPress

[WordPress](https://wordpress.org/) is ubiquitous. You can find cheap, flexible freelancers for occasional changes. You can find cheap, good managed hosting for it. There are plugins to do everything. This keeps your development and maintenance costs low.

Still, WordPress is not perfect. Because of it's popularity, it's a huge target for hackers. Each plugin is a potential security flaw. You need third-party plugins for things that are baked into other CMSes, like custom post types and multilingual content. The codebase is weird and unpleasant to work with.

Nonetheless, it's the best option for you. It's the most cost-effective option, and the most likely to last several years.

WordPress is free. However you might need to pay licence fees for essential plugins.

### Craft CMS

All About Berlin ran on [Craft CMS](https://craftcms.com/) for a few years. It's a lot more pleasant to use than WordPress, both for editors and developers.

However, since it's relatively obscure, you can't rely on a large plugin ecosystem to solve every problem. You must code everything yourself. You won't find experienced Craft developers, so you must hire skilled generalists. These are more expensive and harder to find.

For your project, Craft would cost 399€, then 99€ per year for updates.

### Something custom

You can use a framework instead of a CMS. If you plan to build a *platform*, a framework gives the developers a lot more flexibility.

If you want to build a platform, you can choose something more involved and elaborate. Not a CMS but a framework that you shape into what you want. This is a lot more work, but it leaves an open end for future development.

I don't think this would work well for you, mainly because it would take longer to get the website running, require more specialised labour to build, and likely wouldn't really help.

## Summary and recommendations

Build a simple website that you can easily maintain, using readily available labour. This will keep your maintenance costs low.

Then focus on what matters the most: giving good advice. You need good information more than you need a fancy website.

Don't underestimate the effort it takes to produce quality advice. I had to build a community of practice from the ground up. My work involves dozens of immigration professionals, government employees and industry experts. I also monitor hundreds of pages to know when German bureaucracy changes.

This will require a far greater commitment from you, for a much longer time. Every technology choice that you make should go towards making the editors' work easier, because they will be the ones doing most of the work.

With that in mind, this is how I would prioritise tasks:

1. Build a simple, multilingual, text-based website that is easy to maintain.
2. Implement a [glossary](#10-glossary).
3. Write useful content in [plain language](#6-simple-language).
4. Implement a basic [search](#1-intelligent-search) feature. Do not bother with intelligent or multi-site search.
5. Implement [rich list items](#3-interactive-checklists) to display lists of documents with clear explanations.

This is a short, achievable list of objectives. Start by doing this right, then use your remaining budgets for the following features:

1. Make your editors more productive. Implement [automatic translations](#4-automatic-translations). Use [automated tools](#6-simple-language) to enforce grammar rules, plain writing and other stylistic choices. 
2. Identify which parts of your advice would benefit from [calculators](#8-calculators) and [interactive guides](#2-interactive-guides). Build the most sensible ones, or licence them from Smart Rechner.
3. Implement the feature to save content and remember checklist items that the user ticked.

These are the features I would not implement at all:

1. [Chatbots](#7-chatbots)
2. [Application aid](#5-application-aid)
2. [Intelligent checklists](#3-interactive-checklists)
3. [Intelligent search](#1-intelligent-search)
4. [Multi-site search](#1-intelligent-search)
5. Any AI-based advice