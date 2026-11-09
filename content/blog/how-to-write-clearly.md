---
title: How to write clearly
description: This is an article about technical writing. It lists the tricks I use to write clear instructions for a wide audience. This is how I write guides for All About Berlin.
date_created: 2022-02-10
---

Good documentation helps people feel better about stressful problems. It's is rarely funny or interesting, but it solves your people's problems, and that's important too.

In this guide, I explain how I write about technical topics, and make instructions easy to understand. This is how I write guides for [All About Berlin](https://allaboutberlin.com/).

## Consistency

Use one and only one term to describe something. If you can, use the most popular term.

For example, in Berlin, the Ausländerbehörde is now the Landesamt für Einwanderung. Everyone still calls it the Ausländerbehörde. It's still called the Ausländerbehörde in the rest of Germany. That's why I always call it the Ausländerbehörde in my guides.

If you use terms that your readers don't know, consistency is even more important. If your readers just learned a word, they don't know its synonyms and abbreviations. For example, there are at least 6 different terms for the German tax ID, but I always use "tax ID".

If there are many terms for the same thing, tell it to your readers, then always use the same term. If you use abbreviations, use them consistently. Don't alternate between a term and its abbreviation. You can use [the &lt;abbr&gt; tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr) to clarify them. You can also link to a glossary or a separate article.

![](/images/Screenshot-2021-11-24-at-14.31.34.png)

**Good example:** [What is the tax ID (*Steueridentifikationsnummer*)?](https://allaboutberlin.com/glossary/Steueridentifikationsnummer)

## Precision

Avoid [ambiguous sentences](https://examples.yourdictionary.com/reference/examples/examples-of-ambiguity.html). Don't let your readers guess what you mean. Your writing must be correct, and correctly understood. If the information is not clear, your readers can make bad decisions.

Use the right modal verbs. If you *can* wash your hands, it's optional. If you *should* wash your hands, it's recommended. If you *must* wash your hands, it's required. You can follow[ RFC 2119](http://microformats.org/wiki/rfc-2119). I follow it, but I use "can" instead of "may", because "can" is a [more common](https://en.wikipedia.org/wiki/Most_common_words_in_English#100_most_common_words) word.

**Good example:** [Coronavirus vaccines side effects and safety](https://www.nhs.uk/conditions/coronavirus-covid-19/coronavirus-vaccination/safety-and-side-effects/) - NHS

Bullet lists can be confusing. When you use a list of requirements, tell your readers if they must match one requirement (A *or* B *or* C), or all requirements (A *and* B *and* C).

![](/images/Screenshot-2021-11-24-at-14.41.10.png)

Examples, illustrations and code snippets are very useful. Don't just tell your readers how to do something; show them. Pictures are often the best way to describe what the result should look like.

**Good example:** [How to change Renault Kangoo spark plugs](/blog/renault-kangoo-spark-plugs)

**Best example:** [Cooking for engineers](http://www.cookingforengineers.com/recipe/159/English-Toffee)

Sometimes, a calculator gives better answers than a long text. With a calculator, your readers can quickly get a precise answer. For example, my [health insurance guide](https://allaboutberlin.com/guides/german-health-insurance) gives vague directions in 20 minutes, and my [health insurance calculator](https://allaboutberlin.com/calculators/health-insurance) gives a clear answer in 20 seconds.

![](/images/Screenshot-2021-11-24-at-14.43.30.png)

## Simplicity

> "Get rid of half the words on each page, then get rid of half of what's left."

> — Steve Krug, Don't Make Me Think

Get to the point! Give the shortest complete answer. Don't try to be funny, smart or interesting. Your goal is to solve your readers' problem, not to entertain them.

Keep your introduction short. It should confirm that your reader has found the right page, nothing more. Sometimes, you don't need an introduction at all. A table of contents is an introduction.

You rarely need a conclusion, but a summary can be useful. A ["next steps" section](https://allaboutberlin.com/guides/anmeldung-in-english-berlin#whats-next) can also be useful. Many guides only cover one step in the readers' journey.

**Bad example:** Every recipe website, except [justthefuckingrecipe.net](http://www.justthefuckingrecipe.net/)

Use a simple vocabulary, and write simple sentences. I use [Hemingway](http://www.hemingwayapp.com/) to write more simply. It helps me replace complex words and sentences with simpler ones.

**Good/bad examples:** [Before and after - Plain English Campaign](http://www.plainenglish.co.uk/campaigning/examples/before-and-after.html)

Don't use idioms or expressions. If your readers are not native English speakers, they won't understand baseball metaphors. You should also avoid jokes, sarcasm and commentary, and focus on giving information. Again, your goal is to solve your readers' problems, not to entertain them.

**Bad example:** [How to remove engine ticks](https://www.youtube.com/watch?v=jqADvaRB1YU)

## Structure

Your readers will not read the full article. They will skip sentences, paragraphs, and sections. This is fine. You should help them do it.

Put the short answer (the [tl;dr](https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn%27t_read)) at the top, then add more details. I like to put the short answer in bold at the top. This writing style is sometimes called [Bottom Line Up Front](https://en.wikipedia.org/wiki/BLUF_(communication)) or [inverted pyramid](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)). It's the opposite of clickbait.

![](/images/Screenshot-2021-11-24-at-14.39.20.png)

Structure your content to answer the question step by step. Let your readers decide where to start. A table of contents can help your readers choose where to start.

Use titles, bullet lists, bold text and italics to guide your readers to the answer. Don't force them to read anything that isn't important to them.

If possible, put conditionals ("if you are over 25 years old, ...") at the beginning of the paragraph. This lets your readers skip paragraphs that are not for them. I usually put those conditional statements in bold.

**Good example:** [Cost of public health insurance](https://allaboutberlin.com/guides/german-health-insurance#public-health-insurance), most content on [Finanztip](https://www.finanztip.de/rechtsschutzversicherung/).

Most of my guides have this structure:

1. What is this process
2. Why it must be done
3. How hard it is to do
4. How to do it
5. What to do next
6. Where to find help

When I write troubleshooting guides, I follow another structure:

1. What is the problem
2. How serious it is
3. What the symptoms are
4. Which tools are needed to fix it
5. How I fixed it
6. Things I tried that didn't work

You can make the text easier to read with good typography. You can also create special styles for tips and warnings.

**Good examples:** [Why is my car overheating?](https://www.dummies.com/home-garden/car-repair/why-is-my-car-overheating-and-what-can-i-do/)

## Setting expectations

Your readers [need good information to make good decisions](https://www.nngroup.com/articles/visibility-system-status/). Tell them where they are, where they are going, how long it will take, how much it will cost, and what results to expect. This can save them a lot of stress.

When you can, use precise numbers. For example, liability insurance is very important in Germany: *82% of Germans have it*. German work visas are usually approved *in 8 to 12 weeks*. My dragon noodles recipe takes *30 minutes* to prepare.

When you can't use numbers, use words like "rarely", "sometimes", "usually", "most of the time" and "always". You can also tell your readers [how hard something is](https://allaboutberlin.com/guides/start-a-business-in-germany#is-it-hard-to-start-a-business-in-germany), from "really easy" to "almost impossible". Use a consistent vocabulary for frequency, likelihood and difficulty.

If possible, tell your readers where things can go wrong. Warn them about the scary and stressful parts before they happen.

Sometimes, you need to tell your readers about wrong answers and solutions that don't work. For example, an article about hangover cures should mention common cures that don't work.

**Good examples:**

- [Colostomy: what to expect](https://myhealth.alberta.ca/Health/aftercareinformation/pages/conditions.aspx?hwid=ud1233)
- [All about periods](https://kidshealth.org/en/teens/menstruation.html)
- [Preparing for a first acid trip](https://www.trippingly.net/lsd-studies/2018/7/2/the-first-trip)
- [What happens during your Ausländerbehörde appointment](https://allaboutberlin.com/guides/berlin-auslanderbehorde-same-day-appointment#what-happens-during-your-appointment)

## Revisions

Good documentation happens step by step. You will rewrite your content many times, even after you publish it. I have updated some guides hundreds of times. I have completely rewritten some of them a few times.

Writing clearly is a skill. You get better with practice. Over time, you find better ways to explain things.

As an expert, you can forget how it feels to be a beginner. This is the [curse of expertise](https://en.wikipedia.org/wiki/Curse_of_knowledge). You can learn a lot by listening to your readers, and finding what stresses and confuses them. Their questions are the best feedback you will get.

Over time, you will learn things about your field and about your readers. For example, I know a lot about German immigration, but I know almost nothing about studying or raising children in Germany. I learn about it from my readers. I also learned a lot about the rental market, immigration law, insurance and many other topics.

## Related material

[Communicating with precision](https://pressbooks.bccampus.ca/technicalwriting/chapter/communicatingprecision/) - Technical writing essentials

