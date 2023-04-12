---
title: Playing with data: linking soldiers and war graves
description: Over the past week, I have written about the Canadian Expeditionary Force and the Commonwealth War Graves Commission data sets. After loading both data sets in a common database, it is finally time to bring them together.
date_created: 2016-11-23
---

Over the past week, I have written about the [Canadian Expeditionary Force](http://nicolasbouliane.com/blog/parsing-575k-military-records-with-python) and the [Commonwealth War Graves Commission](http://nicolasbouliane.com/blog/the-commonwealth-war-graves-commission-data-set) data sets. After loading both data sets in a common database, it is finally time to bring them together.

## Meet John Smith

One table contains the records of every enlistee in the Canadian Expeditionary Force. The other contains records of every known First World War grave of Canadian soldiers.

A naïve approach to this problem would be to use the name to join the tables. A man who enlisted as John Smith likely has John Smith written on his grave, right?

Well... yes (actually no, but more on that later), but there were 172 John Smiths in the Canadian Expeditionary Force. In fact, there were 17646 Johns and 6498 Smiths on record. In fact, the Johns accounted for 3% of all the Canadian Expeditionary Force.

The Johns could form a division to themselves. As such, first and last names alone cannot be used to differentiate enlistees.

Fortunately, we have other useful information to tell apart our 172 John Smiths.

## Regimental numbers

First, let's have a look at the ID-like values we have in each table. Both tables have a [regimental number](http://www.collectionscanada.gc.ca/obj/001042/f2/Regimental_Number_List_of_the_Canadian_Expeditionary_Force.pdf) column. It is called a service number in the war graves table, but a little research confirms that it's simply a more recent term for regimental numbers.

Each man in the Canadian Expeditionary Force was assigned a regimental number, save for nursing sisters and commissioned officers. Each unit had a block of regimental numbers it would assign sequentially to its enlistees. As the [Library and Archives Canada documentation](http://www.collectionscanada.gc.ca/obj/001042/f2/Regimental_Number_List_of_the_Canadian_Expeditionary_Force.pdf)points out, enlistees with sequential numbers were likely standing next to each other in line at the recruiting booth. This changed in 1917, as numbers were from then on assigned to men in the order in which they were called up for service.

Members of the Royal Newfoundland Regiment did not receive numbers, as they were not part of the Canadian Expeditionary Force (Newfoundland joined Canada in 1949).

Regimental numbers might appear to be great candidates for identifying soldiers, but as Michael O'Leary from The Regimental Rogue [points out](http://regimentalrogue.com/misc/researching_first_world_war_soldiers_part10.htm), these numbers were frequently reassigned to multiple enlistees across the nation, and not every unit assigned numbers within their assigned blocks.

Our data set supports this claim. Some regimental numbers appear over a dozen times in the CEF data set. There are also several thousand records without regimental numbers.

Moreover, many enlistees have more than one regimental number. The most likely reason is that these enlistees were transferred during the war.

## Michel, Mike and Michael

Despite the lack of a proper unique identifier for enlistees, it might still be possible to link *some*records.

Some people might share the same regimental number, so let's only merge records where the names match.

<table><thead><tr><th>Criteria for merging</th><th>Merged records</th></tr></thead><tbody><tr><td>Same regimental number</td><td>69 270 (100%)</td></tr><tr><td>Same regimental number and last name</td><td>50 693 (73%)</td></tr><tr><td>Same regimental number and first name</td><td>25 586 (37%)</td></tr><tr><td>Same regimental number, first name and last name</td><td>23 319 (34%)</td></tr></tbody></table>

By matching only by regimental number, we get more matches than we have war graves, which means several graves match more than one enlistees. The next step is to match soldiers that have the same regimental number, first name and last name.

At a glance, it seems like most records have mismatching first names. A quick look at the mismatching records reveals that empty first name values caused 70% of the first name mismatches.

<table><thead><tr><th>CEF first name</th><th>CWGC first name</th></tr></thead><tbody><tr><td>CHARLES JOHN</td><td>(null)</td></tr><tr><td>JOHN BAPTIST</td><td>(null)</td></tr><tr><td>JOHN JOSEPH</td><td>(null)</td></tr><tr><td>PERCY PHILLIPS</td><td>(null)</td></tr><tr><td>JAMES</td><td>(null)</td></tr><tr><td>JAMES</td><td>(null)</td></tr></tbody></table>

The remaining first name mismatches seem primarily caused by spelling differences and middle names.

<table><thead><tr><th>CEF first name</th><th>CWGC first name</th></tr></thead><tbody><tr><td>REGINALD SYDNEY</td><td>REGINALD SIDNEY</td></tr><tr><td>LEONARD J</td><td>LEONARD JAMES</td></tr><tr><td>HAROLD</td><td>HAROLD CHARLES</td></tr><tr><td>MATTHEW HUMPHREY</td><td>MATHEW HUMPHREY</td></tr><tr><td>JOHN</td><td>JOHN RICE</td></tr><tr><td>WALTER WILLINGALE</td><td>WALTER W.</td></tr><tr><td>RUSSELL KIRBY</td><td>RUSSELL KERBY</td></tr><tr><td>ERNEST</td><td>ERNEST LESLIE</td></tr><tr><td>CLIFFORD H</td><td>CLIFFORD H.</td></tr><tr><td>ALFRED GEORGE EDWARD</td><td>ALFRED G. E.</td></tr><tr><td>HAROLD</td><td>HAROLD BAKER</td></tr></tbody></table>

However, matching by last name alone is a very bad idea, not to mention that they are also prone to spelling differences.

## John Smith and John Smith

In addition to these inconsistencies, I discovered that several people with the same first name, last name and regimental number in the Canadian Expeditionary Force data set.

```
<span class="hljs-operator"><span class="hljs-keyword">SELECT</span> regiment_nr1, surname, given_name, <span class="hljs-keyword">count</span>(*)
<span class="hljs-keyword">FROM</span> cef_enlistees
<span class="hljs-keyword">WHERE</span> regiment_nr1 <span class="hljs-keyword">IS</span> <span class="hljs-keyword">NOT</span> <span class="hljs-literal">NULL</span>
<span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> regiment_nr1, surname, given_name
<span class="hljs-keyword">HAVING</span> <span class="hljs-keyword">count</span>(*) > <span class="hljs-number">1</span>
<span class="hljs-keyword">ORDER</span> <span class="hljs-keyword">BY</span> <span class="hljs-keyword">count</span>(*) <span class="hljs-keyword">DESC</span></span>
```

It would be easy to dismiss these as duplicates, but there were indeed [two men](http://www.bac-lac.gc.ca/eng/discover/military-heritage/first-world-war/personnel-records/Pages/list.aspx?SurnameSearch=DEGRE&GivenNameSearch=LIONEL&) named Lionel Degre with the same name regimental number. Perhaps this is a transcription error, but they do have distinct documents.

In other cases, there are indeed duplicates. [Stephen James Burns](http://www.bac-lac.gc.ca/eng/discover/military-heritage/first-world-war/personnel-records/Pages/list.aspx?SurnameSearch=BURNS&GivenNameSearch=STEPHEN%20JAMES&) appears twice in the database, but both records share the same enlistment papers (based on URL) and birth date.

There are only 70 such duplicates in the database, and many of them can be eliminated by comparing their birth dates and document URLs. We can simply avoid merging war grave records for the remaining duplicates, if they exist.

## More problems

According to [the official documentation on regimental numbers](http://www.collectionscanada.gc.ca/obj/001042/f2/Regimental_Number_List_of_the_Canadian_Expeditionary_Force.pdf), a soldier can have multiple numbers following a unit transfer during the war. In the original database schema, is stored multiple numbers in separate columns, and that prompted me to store the regimental numbers in a separate table.

## Intermission

What have we learned so far?

- First names and last names are not unique.
- Regimental numbers are not unique, either, but they can help differentiate people with the same name.
- The same person can have its name spelled differently in different data sets.
- A combination of first name, last name and regimental number is not unique either, but such combinations are fairly rare. We can still merge a few thousand other records.

## Battle plan

With a better idea of what we are dealing with, it's time to formulate a plan.

First, let's eliminate duplicates in the Canadian Expeditionary Force data set. This will be added to the import script so that we don't have to worry about this in the future.

Second, let's go for the easy victories and merge CEF and CWGC records that have the same first name, last name and regimental number, except for those who are in our list of duplicates.

Third, merge CEF and CWGC records that have variations of the same first and last name using fuzzy matching. More on that later.

## To be continued

The methods I used to eliminate duplicates are worth their own article, so I decided to cut this article in half. In the meantime, have a look at the [GitHub repository](https://github.com/nicbou/canadians-at-war) for this project. Every operation I performed on the database are reproducible by using the code hosted there, so I invite you to have a look.

