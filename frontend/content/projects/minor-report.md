---
title: Feasibility study: Berlin Welcome Center
description: A feasibility study for the new website of the Berlin Welcome Center.
date_created: 2025-02-01
---

This is a feasibility study for a new website for the Berlin Welcome Center. The Welcome Center is a counselling centre for recent immigrants. It is managed by the *[Senat für Partizipation, Integration und Migration](https://www.berlin.de/lb/intmig/)*.

{% include "blocks/_tableOfContents.html" %}

## Foreword

### Budget assumptions

In this report, I prioritised the impact and longevity of the project, given an initial budget of around 50,000€. I assumed that there will also be a smaller yearly budget for maintenance and further development. I also assumed that this budget is subject to political winds, so I favoured low maintenance costs wherever possible.

### Simple is cheap

There is a common theme in this report: software is complex, and complexity is expensive. Add as little complexity as you need to get the job done.

A text-based website is cheap to build, maintain and adapt. Once the website is built, anyone can work on the content. Such websites can run forever with minimal maintenance. The only downside is the user experience. Text takes more effort to read and understand.

Software is the opposite. Good software saves time and offers a magical user experience. However, it's much more expensive to build, adapt and maintain, especially if you outsource the technical work. You must allot time and money to server upkeep, software updates, and so on. Software is a commitment, and its upkeep is a tax.

### Bet on text

Text is very flexible. It can be cited, linked to, emailed and printed. It can be found through Google, archived, subscribed to, saved for online reading, translated, summarised by AI and read by accessibility tools. It can automatically be turned into PDFs, newsletters, flyers e-books and podcasts.

Due to its simplicity, text is easy to migrate between platforms. There are countless tools to work with text.

More often than not, text is a much better choice than software.

### Castles on quicksand

You can't build a rigid digital layer on top of an unpredictable analog bureaucracy.

German bureaucracy is too arbitrary and inconsistent to describe with code. Each Bezirk, each Amt and each Beamter interprets the law differently. They make arbitrary decisions based on undocumented policies that change without warning. This is not a stable foundation to build rigid software upon.

Bureaucracy is also really hard to observe. For All About Berlin, I rely on a large network of people that took years to build. I use scripts to watch hundreds of pages for changes. Even with that infrastructure, it can take weeks to notice, understand and document changes in policy.

Consider that German bureaucracy might change faster than you can adapt the software that you have built. Text is much cheaper to adapt than software.

### Sheds and skyscrapers

Complex projects require specialised labour. Specialised labour is more expensive and harder to find.

You can easily find freelancers to work on a WordPress website. It might be harder to find maintainers for your fancy technology stack. It's even harder if you can't pay market rates, or if you only a developer for a few hours every now and then. Maintaining complex software can become a human resources problem.

[Choose boring technology](https://mcfunley.com/choose-boring-technology), especially if you don't have an in-house development team to maintain it.

## 1. Intelligent search

### 1. Description

> ‘Intelligent’ search field with filter options to personalise results (e.g. by nationality, residence status, language, etc.) as well as automatic completion of the search query and correction of spelling errors to improve accuracy

This feature is about a search box that helps users efficiently find content on the website. It should return content in the user's language, and possibly include a sort of autocomplete feature.

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

Artificial intelligence builds upon good search, which builds upon good content.

Retrieval-augmented generation (RAG) is a hybrid of search and AI. AI can't fit your entire website into its brain, so it searches your content and summarises the first few results. RAG only works if its built on top of a good search. AI can only generate answers from your content if it finds it.

RAG is a common technique used in developing expert AI. It would likely be used if you develop a chatbot, AI search and other AI tools. In other words, before you build a good AI, you must build a good search.

### 4. Feasibility assessment

#### Search

Search is a feature. Good search is a project. Given your budget, aim for "good enough".

Lexical search is good enough, and it's very easy to implement. It meets most people's expectations, especially on a small website with a few hundred pages. It's also easy to suggest different types of results in the search bar (categories, tags and pages), like in the CityLab prototypes.

Semantic search is possible, but it's more work. There are off-the-shelf solutions for this, but they must be implemented, then customised and adjusted to your needs. This can take significant development time.

[Algolia](https://www.algolia.com/) and [ElasticSearch](https://www.elastic.co/enterprise-search/) are two of the biggest providers. You feed them your documents, and they give you a search box. These solutions are deployed by large organisations to search across many departments and websites. These solutions are overkill for your needs.

[Google Programmable Search Engine](https://programmablesearchengine.google.com/about/) could also work. It's basically search results from Google, but limited to your website. It's halfway between basic lexical search and the fully customisable experience of other off-the-shelf solutions.

Global search across multiple websites is much more difficult. You would need to crawl all those websites yourself, filter out useless pages, evade anti-bot measures, and figure out how to rank those results. Then you would definitely need tools like Algolia or ElasticSearch. You would effectively build your own little search engine. This is well beyond your budget.

Search can always be improved later. Implement basic lexical search now, gather usage data, and improve it later as needed. Semantic search might stretch your budget. AI search would definitely exceed it.

#### Filtering

Filtering is easy to implement. Most CMSs provide utilities that make it possible. Returning different *kinds* of results (categories, tags, guides, articles, document templates) is also easy to implement.

To get good filters, you need good metadata. Filters only work when every page is correctly tagged, categorised, and all the fields are correctly filled in. The search filters of an online store only work if the metadata for every product is meticulously filled in. You can only filter clothes by colour because someone added colour data to every product.

![Amazon product filters](/images/product-filters.png "Product filters require detailed product data")

In your case, this means carefully considering how you organise, categorise and tag your content. Consider how much effort this could mean for your editors.

For example, to filter information by nationality, you must manually tag every page with the nationalities it applies to. If this information changes, all pages must be re-tagged without making any errors. This happens often! The United Kingdom left the EU. Romania joined the Schengen Area. Montenegro signed a pension agreement with Germany. Someone must update that data everywhere, every time, forever. Will enough people use the search filters to make this worthwhile?

I suggest filtering by simple taxonomies like category, responsible *Amt*, language and tags. You likely need to create those taxonomies to organise the content on your website anyway.

### 5. Risks and challenges

Semantic search is harder to get right. It might not work well when mixing multilingual content with specialised German terms. A search engine might understand the proximity of the words "king" and "prince", but it might not understand the relationship between "Anmeldung", "Meldebescheinigung" and "Meldebestätigung" for example, especially not in an English-language document. Likewise, if someone searches for "LEA", it might not return results for "Landesamt für Einwanderung" unless both terms are in the same document.

Content can only be searched for if it's indexed. All the text in an article is searchable. The title, description, tags and categories are usually searchable. The text inside interactive tools might not be searchable - neither by our internal search nor by search engines like Google. In that sense, interactive tools can make your advice harder to discover.

It's possible that nobody really uses your search feature. All About Berlin gets 7 searches for every 1,000 visits. If most of your visitors come directly to the right page from Google, search engine optimisation is a better investment.

## 2. Interactive instructions

### 1. Description

> Clickable, interactive and customisable (e.g. according to the languages spoken, residence status, length of stay, etc.) step-by-step instructions that guide users through bureaucratic processes in a simple and understandable way.

This feature is about creating an interactive guide to navigate users through bureaucratic processes. You build tools that help them navigate [decision trees](https://en.wikipedia.org/wiki/Decision_tree). You ask them questions, and their answers lead them to a recommendation. This is an improvement over simple text instructions.

Let's call those tools "interactive guides".

### 2. Technical requirements

You can create interactive guides one by one, as bespoke software. This is the approach I take.

Your content editors might want to build tools themselves. They could create and update interactive guides without hiring expensive software developers every time. A tool could help them create flowcharts, and automatically turn those flowcharts into an interactive guide for the website.

For this, they would need *no-code tools*.

### 3. Artificial intelligence

I see no applicable use for AI here. These tools navigate users through rigidly-defined processes. There should be no uncertainty, and no room for an AI to guess what to do. AI advice is error-prone, difficult to test, and likely to give incorrect advice the appearance of trustworthiness.

### 4. Feasibility assessment

Each interactive guide is its own mini project with its own requirements.

I need two to six weeks to build a interactive guide. The first tool takes longer to build, because developers must build the groundwork that is reused for each tool afterwards.

It might take longer in your case, because the work is defined by one team and done by another. It also takes time to understand and define the logic behind each tool. If that knowledge comes from a third team, it adds more delays.

There might be off-the-shelf solutions to create interactive guides without coding. If these tools exist, they might require significant development time to adapt to your needs.

There is [Floma](https://floma.io/), a tool built for the calculator on [Mietencheck.de](https://mietencheck.de/), but it's not mature software yet. The closest mature solution is [VisiRule](https://www.visirule.co.uk/solutions/decision-tree-flowcharts), but it might not do exactly what you need.

In my opinion, this feature is not achievable within your budget. Bespoke interactive guides are expensive to build. A tool that lets you build your own interactive guides is several times more expensive, and might still fail at its task.

### 5. Risks and challenges

Translating those interactive guides adds a layer of complexity. Every question, answer and verdict must be translated to multiple languages. If you choose the no-code route, it will be hard to do this through an intuitive user interface.

Interactive guides need regular maintenance. Bureaucratic processes change often and without warning. The changes might require a complete overhaul of your tools. There is also a lot of variance in German bureaucracy. It might not be possible to describe things as a simple flowchart with a well-defined outcome.

Search engines only index what they can see. They do not see the useful information buried multiple steps deep into an interactive guide. Interactive guides make information less discoverable for people using Google, ChatGPT or your own search. You might need to maintain two versions of your advice: a text version, and an interactive guide.

Making software accessible is much harder than making text content accessible.

See ["Castles on quicksand"](#castles-on-quicksand).

## 3. Interactive checklists

### 1. Description

> Clickable, interactive and customisable (e.g. according to the languages spoken, residence status, length of stay, etc.) step-by-step checklists to support users in preparing documents to be submitted for applications or in checking the requirements.

This feature is about offering smart lists of documents. There are two ways to imagine this:

- **Make the list smart**  
    The user enters information about themself, and they get a personalised list of instructions or documents to prepare, based on their situation.
- **Make the elements more useful**  
    A regular list, but the list elements are more than just text. For example, they can have a "?" button that explains what the document is and where to find it. The list could show previews of the document or link to a PDF template. The editors can create those rich list items and reuse them in multiple lists.

### 2. Technical requirements

The requirements for an interactive checklist are the same as for interactive instructions. Each interactive checklist is its own mini project. You must figure out all the possible checklist combinations and build the logic to display them. Then you are no longer writing text, but programming rules. You are writing software. Once again, you can pay software developers to do it every time, or pay a much higher price to let them build software to edit the list yourselves.

Rich list elements are much easier to make. They are just a nice way to present the information. You create documents using the CMS, and you insert a list of those documents in your posts. We can present these documents however we want: in a collapsible panel, with a little information bubble, etc.

### 3. Artificial intelligence

Artificial intelligence can be used to quickly add a lot of information about a long list of documents. However, AI generated content tends to be too vague to be useful, and too inaccurate to be trustworthy.

### 4. Feasibility assessment

Interactive checklists are not achievable within your budget. They work exactly like interactive instructions, and they are unachievable for the same reasons.

Rich list elements are possible, and very easy to implement. This feature is well within your budget.

Still, consider that for this purpose, plain text could be enough. It's more important to have good, reliable information than to present it slightly better.

### 5. Risks and challenges

Requirements are not fixed in stone. They vary by office, department and case worker. They change without warning, and are rarely well-documented. The official information on Berlin.de is often incorrect. Gathering correct information is a lot more work than choosing how to present the information.

See ["Castles on quicksand"](#castles-on-quicksand).

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

: filling the form, sending the form, making the payment, getting status updates, receiving the desired document 

### 3. Artificial intelligence

### 4. Feasibility assessment

Berlin does not offer an API for its digital processes. For the most part, Berlin does not offer digital processes. It's mostly analog processes over email.

For every step of the process, you must create scripts that mimic the actions of a human: clicking around, downloading forms, filling PDFs, sending emails and making payments.

The response from the bureaucracy is not an instant, predictable, machine-readable message. A human will write a unique letter and mail it to user's home address in 4 to 8 weeks.

Each of the 12 districts handles bureaucracy in its own way, with varying requirements and varying efficiency. You must either adjust your automated solution to the whims of each district, or send all your applications to a single district. In my experience, no district will volunteer for this.

The few existing digital processes only work with BundID, which most immigrants can't use, and which your scripts can't work around.

Put simply, Berlin's bureaucracy is actively hostile to automation. In any case, this feature would not be achievable within your budget.

### 5. Risks and challenges

See ["Castles on quicksand"](#castles-on-quicksand).

## 6. Simple language

### 1. Description

> Automatic translation of content (text content, infographics, explanatory videos) into simple language and switching between complex language and simple language to ensure low-barrier accessibility

This feature is about automatically translating the content to plain language.

### 2. Technical requirements

The requirements, methods and challenges are exactly the same as for [automatic translations](#automatic-translations). For the most part, you can treat simple language as just another language.

### 3. Artificial intelligence

Artificial intelligence can aid writers by making suggestions as they type. The quality of the advice varies wildly from valid suggestions to hallucinated corrections, so human judgement is needed.

### 4. Feasibility assessment

Plain language [benefits everyone](https://www.nngroup.com/articles/plain-language-experts/) and should be the default.

AI and non-AI tools can be used to highlight passages that need improvement. It can suggest better ways to write. However, AI cannot be trusted to simplify text without losing important context.

AI tools can aid skilled editors with plain writing, but they can't replace skilled editing work. These tools don't need to be integrated in your CMS; they just need to be available to your editors. I would suggest simply making [Deepl Write](https://www.deepl.com/de/write), [Language Tool](https://languagetool.org/de), [Hemingway](https://hemingwayapp.com/) or [Grammarly](https://www.grammarly.com/) available to your editors, and making plain writing part of your style guide.

![Deepl Write](/images/deepl-tones.png "Deepl Write helps you write in plain language.")

### 5. Risks and challenges

See "[automatic translations](#automatic-translations)".

## 7. Chatbot

### 1. Description

> Recording the questions, profiles (e.g. nationality, residence status, language, etc.) and counselling needs of those seeking advice by questionnaire and by chat or clickbot in order to be able to offer personalised information and referrals or to narrow them down to the specific situation.

### 2. Technical requirements

### 3. Artificial intelligence

### 4. Feasibility assessment

### 5. Risks and challenges

## 8. Calculators

### 1. Description

> Calculator (e.g. for living costs, financial support, housing benefit, etc.) with personalisation functions using filters to estimate costs or financial support in your own situation.

See [interactive instructions](#interactive-instructions). The work, the challenges and the costs are almost the same.

### 2. Technical requirements

### 3. Artificial intelligence

I see no applicable use for AI here. These tools navigate users through rigidly-defined calculations. There should be no uncertainty, and no room for an AI to guess what to do. AI calculations are error-prone, difficult to test, and likely to give incorrect calculations the appearance of trustworthiness.

## 9. Saved content

### 1. Description

> Saved search and favourite services (with and without user account) to quickly retrieve relevant content (including step-by-step instructions and checklists in progress, see 2 and 3)

### 2. Technical requirements

### 3. Artificial intelligence

### 4. Feasibility assessment

### 5. Risks and challenges

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

## API access

None of the listed elements offer an API. These websites are not designed to be operated by other machines. Many of those website implement anti-bot measures. They either limit the rate of requests, or block bots outright.

As explained in the [application aid](#application-aid) section, the planned feature is not feasible with the allocated budget.

## Additional requirements

### 1. Mobile first

Mobile-first design has been the standard for over a decade. It is expected that the website must adapt to mobile screens.

### 2. Multilingual content

This has been covered in more details in the [automatic translations](#automatic-translations) section.

We have mature tooling to build multilingual text-based websites. However, it adds a layer of complexity to any tool that you choose to build.

The hardest part is simply maintaining one version of your content for each language, and keeping those in sync. Tools exist to make this easier, but it cannot be entirely automated.

### 3. Accessibility

A basic level of accessibility can be expected, but full WCAG compliance is harder, especially if it's not part of the entire design process from the start.

The choice of technology has less impact on accessibility, but the complexity of what you build does. It's easy to make text accessible. It's much harder to make software accessible.

Talk to the *[Landesbeauftragte für digitale Barrierefreiheit](https://www.berlin.de/lb/digitale-barrierefreiheit/)* and the [ITDZ accessibility team](https://www.itdz-berlin.de/allgemeines/digitale-barrierefreiheit/). They might save you a lot of guesswork.

### 4. Privacy

GDPR (DSGVO) is only a concern if you collect data about your users. This can happen if you track your users, or if you collect and store information about them through forms, user accounts or cookies. The easiest way to conform to data protection laws is to not collect any data.

You can still collect anonymous statistics while respecting the GDPR. Your statistics lose some precision and granularity, but they give you sufficient insight into your user base.

You can also collect personal data, so long as you collect it with consent, use it for its intended purpose, store it securely and delete it when it's no longer needed.

## Available options

For your needs, I would consider WordPress or Craft CMS.

### WordPress

[WordPress](https://wordpress.org/) is ubiquitous. You can find cheap, flexible freelancers for occasional changes. You can find cheap, good managed hosting for it. There are plugins to do everything. This keeps your development and maintenance costs low.

Still, WordPress is not perfect. Because of it's popularity, it's a huge target for hackers. Each plugin is a potential security flaw. You need third-party plugins for things that are baked into other CMSes, like custom post types and multilingual content. The codebase is weird and unpleasant to work with.

Nonetheless, it's the best option for you. [why]

WordPress is free. However you might need to pay licence fees for essential plugins.

### Craft CMS

All About Berlin ran on [Craft CMS](https://craftcms.com/) for a few years. It's a lot more pleasant to use than WordPress, both for editors and developers.

However, since it's relatively obscure, you can't rely on a large plugin ecosystem to solve every problem. You must code everything yourself. You won't find experienced Craft developers, so you must hire skilled generalists. These are more expensive and harder to find.

For your project, Craft would cost 399€, then 99€ per year for updates.

### Something custom

You can use a framework instead of a CMS. If you plan to build a *platform*, a framework gives the developers a lot more flexibility.

If you want to build a platform, you can choose something more involved and elaborate. Not a CMS but a framework that you shape into what you want. This is a lot more work, but it leaves an open end for future development. I don't think this would work well for you, mainly because it would take longer to get the website running, require more specialised labour to build, and likely wouldn't really help.

## Summary and recommendations

Build a simple website that you can easily maintain, using readily available labour. This will keep your maintenance costs low.

Then focus on what matters the most: giving good advice. You need good information more than you need a fancy website.

Don't underestimate the effort it takes to produce quality advice. I had to build a community of practice from the ground up. My work involves dozens of immigration professionals, government employees and industry experts. I also monitor hundreds of pages to know when German bureaucracy changes.

This will require a far greater commitment from you, for a much longer time. Every technology choice that you make should go towards making *that* work easier.