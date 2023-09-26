---
title: Appointment finder
description: A tool that helps you grab one of those elusive Bürgeramt appointments.
date_created: 2022-02-22
project_url: https://allaboutberlin.com/tools/appointment-finder
repo_url: https://github.com/nicbou/burgeramt-appointments-websockets
---

Most of the German bureaucracy happens in person, by appointment. In 2022, I made [an open-source bot to help people find appointments](https://allaboutberlin.com/tools/appointment-finder) at the Bürgeramt. This helps recent immigrants [register their address](https://allaboutberlin.com/glossary/Anmeldung) faster, so that they can access other government services.

**[Try the tool](https://allaboutberlin.com/tools/appointment-finder)** or [see the code on GitHub](https://github.com/nicbou/burgeramt-appointments-websockets).

![The Bürgeramt appointment finder UI](/images/appointment-finder.png)

This post explains why I built this tool, and how I got it approved by the city of Berlin.

{% include "blocks/_tableOfContents.html" %}

## What's wrong with Bürgeramt appointments?

In Berlin, most government services require you to go to the Bürgeramt in person. To do this, you need an appointment.

**Bürgeramt appointments are hard to find**. Most of the time, there are no appointments.[^0] You must refresh the page again and again until you find one. Since most appointments are added during working hours,[^1] many Berliners must do this during work.

![Berlin.de showing no available appointments](/images/berlin-buergeramt-termin-kalender.png "No appointments. Typisch Berlin.")

Most of the time, **the only appointments are in 6 to 8 weeks**.[^2] Recent immigrants can't wait this long to register their address because it blocks other things. They need a [registration certificate](/glossary/Anmeldebest%C3%A4tigung) and a [tax ID](/glossary/Steueridentifikationsnummer) *right now*.

If you can't wait, you can't be picky about location. This means that you might need to go to a Bürgeramt across the city in the middle of a workday.

People can't predict their schedule 6 to 8 weeks in advance, so many people miss their appointments.[^3] In some districts, 20% of people don't go to their appointments.[^4]

**The lack of appointments affects everyone**. Travellers can't leave Germany because they can't renew their passports.[^6] Immigrants must pay the maximum income tax rate because they don't have a tax ID. Parents can't apply for Kindergeld because they can't register their address. Car buyers can't drive their vehicle because they can't register it.[^5] These delays cause serious problems.

## Why are there no appointments?

This has been a problem for many years. There was a noticeable improvement in the last two years, but it's still a serious problem. The reasons have not changed.[^26]

### Personnel shortage

There are not enough Bürgeramt employees to help everyone.[^7] Many employees retire and must be replaced.[^10] There are still many vacant positions, and not enough budget to hire new employees. The government promises to hire more personnel, but the situation does not improve.[^8]

The population of Berlin grows quickly, and more people need government services.[^9]

### Inefficiency

Bürgeramt appointments take time. A Bürgeramt employee only handles 18 cases per day.[^15] Adding more people helps, but it does not solve this problem.

To make things worse, a thousand Berliners miss their Bürgeramt appointment every day.[^16] In Pankow, 10% don't go to their appointments. In Neukölln, it's 20%.[^17] Two separate city employees hinted that these numbers are conservative.

It could be that people forget their appointments, or that their plans change and they can't go. There are no appointment reminders. An email and SMS reminder system was announced in 2018,[^18] but it's still missing. They also considered making the cancel button more prominent in the confirmation email, but this yet has to be done.

Some measures were taken to reduce the rate of no-shows, but the city government can't ban people, nor set up countermeasures that would disadvantage people. For example, the idea of a refundable deposit was rejected.

### Hidden appointments

The Bürgeramt does not make all appointments available online. They keep free appointments. Some are only available to people who call [115](https://allaboutberlin.com/glossary/B%C3%BCrgertelefon). Others are not available at all, and given by Bürgeramt employees at their discretion.

This means that many appointments are impossible to get through the official website. People have received appointments on the same day by faxing their local Bürgeramt. The fax trick was much publicised in the summer of 2023.

### When will things change?

Every new government promises to work on this, including the current government. More employees, more digitalisation, longer opening hours.[^19]

Digitisation will help, but it's happening very slowly.[^20] More and more services are available online,[^21] but essential services still require a Bürgeramt visit. Some online services require a digital ID,[^22] which many immigrants are still waiting for.

In mid-2023, the IKT-ZMS updated the official appointment page, but only to limit everyone to one page refresh per minute. This bot prevention measure makes the website even more unusable for humans. A "[Verschlimmbesserung](https://en.wiktionary.org/wiki/Verschlimmbesserung)", as the Germans say.

![Rate limiting on the Berlin.de appointment booking page](/images/berlin-buergeramt-no-appointments.png)

In September 2023, they suggesting letting people show up without an appointment. Instead of waiting 6 weeks at home, you could wait 6 hours in a crowded the Bürgeramt, just like we did back in 2015.[^11]

The online address registration should come in 2024, but it will require a digital ID that immigrants don't have for a few months. Activating that ID requires an in-person appointment.

## What this tool does

It checks the Berlin.de [appointments page](/out/appointment-anmeldung) every 3 minutes. When it finds new appointments, it broadcasts them to everyone who has the tool open in their browser.

![The Bürgeramt appointment finder UI](/images/appointment-finder.png)

If the tool is open in another tab, it will play a sound and change the tab title when new appointments are found. This is important because people can wait hours for new appointments.

![The Bürgeramt appointment tab notification](/images/appointment-finder-tab.png)

If there are no appointments, I show people other ways to find one.

![The Bürgeramt appointment finder UI](/images/appointment-finder-empty.png)

The tool makes the same number of requests, no matter how many people use it. It uses websockets to broadcast what it finds. It does not increase the load on Berlin.de's servers; it reduces it.

The tool is free and [open source](https://github.com/nicbou/burgeramt-appointments-websockets). The goal was maximum availability. I designed it to be easy to run yourself with limited computer skills. You can `pip install` it, and run it with a single command: `appointments`. The command line version can also play sounds.

![The command line version of the Bürgeramt appointment finder](/images/appointment-finder-cli.png)

### Limitations

When I launched this tool in January 2022, it stayed online for only 7 hours. I deactivated it when I learned that it broke Berlin.de's rules. In those 7 hours, it got thousands of visitors, mentions in the newspapers,[^24] and a strong reaction on social media.[^25]

I contacted the IKT-ZMS team - the people who build the official appointment booking system - and asked them if I could reactivate the tool. They said yes, if I only poll Berlin.de every 3 minutes (instead of every 30 seconds). This makes the tool less useful, but it still works.

Since I can't check more appointment types or get more information from the websites without making more requests, the tool is effectively limited to its current state.

It's not possible to check for other types of appointments, or to filter appointments by location. That would require making more requests, and I can't do that.

I asked the IKT-ZMS team to unlock more appointment types, but they have been completely unresponsive. After months of trying, I gave up.

## Why I built this

It's a small act of [guerilla public service](https://99percentinvisible.org/episode/guerrilla-public-service/). I moved to Berlin in 2015. Since 2017, I run a website to help immigrants make Berlin their home. It's frustrating to see them have the same problems I had 7 years ago. I wanted to build something useful and draw attention to the problem.

The tool did get [a bit of media attention](https://web.archive.org/web/20211018133143/https://www.rbb24.de/panorama/beitrag/2021/10/termin-buergeramt-berlin-software-tipp.html), and the link is still bouncing around immigrant communities. Hundreds of people use it every day.

Still, the problem is not solved. In the long term, we should fix Berlin's administration, not build hacks around it.

### Is this ethical?

**I'm not sure.** This tool does not create more Bürgeramt appointments. It makes it easier for people who use the tool, but also harder for those who don't. It does not solve the appointment problem. Only the city of Berlin can do that.

Then again, anyone can use this tool. It's completely free. It does not ask for your email, it does not collect your personal data, and it does not try to sell you something. In 2015, a startup built a similar tool, and used it to sell appointments for 45€ each.[^23] Now, a similar startup sells Ausländerbehörde appointments for 50€.

This tool is different: it does not have a business model. It's meant to be free for everyone. This played a big role in getting the tool approved by the city.

## What will happen next?

**Nothing**. The tool has been running smoothly for the last two years, but it's crippled by the 3 requests per minute rule.

I want to work with the IKT-ZMS team to improve Berlin.de directly. This includes a better user interface and clearer instructions. So far, I was not successful. I have tried again and again to work with them, but had to accept that my efforts were in vain.

Nonetheless, I am thankful for their time. They agreed to meet me, and one of them worked with me on a connection issue between my tool and their website. He's the one who put me in touch with that team in the first place.

Another kind government employee from a different team showed me how the appointment system works on their side. He was very generous with his time and helped me find the right people to contact in the city government. He is still my most treasured contact there and I am very grateful for his help.

There is also hope from the fringes of government: my old colleagues are lifting mountains in the [Digital Service](https://digitalservice.bund.de/), as are the people at [CityLab](https://citylab-berlin.org/de/start/).

[^0]: [plus.tagesspiegel.de](https://www.tagesspiegel.de/der-graue-lappen-ist-zuruck-die-jagd-nach-dem-internationalen-fuhrerschein-wird-zum-sussen-nostalgie-erlebnis-336706.html), [tagesspiegel.de](https://www.tagesspiegel.de/berlin/keine-losung-fur-terminstau-bei-berliner-burgeramtern-4256614.html), [checkpoint.tagesspiegel.de](https://checkpoint.tagesspiegel.de/langmeldung/zeWyOidG3PriBabT5nd8b)
[^1]: [nicolasbouliane.com](https://nicolasbouliane.com/blog/berlin-buergeramt-experiment)
[^2]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlins-innensenator-schlagt-zentralisierung-der-burgeramter-vor-5607997.html)
[^3]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlin-will-termine-vorerst-nur-per-telefon-vergeben-5201707.html#:~:text=wo%20sechs%20monate%20im%20voraus%20termin-fixierung%20moglich%20sei%2C%20steige%20au%C3%9Ferdem%20die%20ausfall-%20und%20vergessensquote%20erheblich)
[^4]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlins-innensenator-schlagt-zentralisierung-der-burgeramter-vor-5607997.html#:~:text=jeder%20zehnte%20termin%20werde%20dadurch%20in%20pankow%20nicht%20wahrgenommen.%20in%20neukolln%20seien%20es%20sogar%2020%20prozent.), [rbb24.de \(archived\)](https://web.archive.org/web/20220104195144/https://www.rbb24.de/politik/beitrag/2021/06/berlin-terminmangel-laengere-oeffnungszeiten-buergeraemter.html)
[^5]: [bz-berlin.de](https://www.bz-berlin.de/berlin/auto-anmeldung-dauert-in-berlin-bis-zu-zwei-wochen), [tagesspiegel.de](https://www.tagesspiegel.de/berlin/schlange-stehen-in-der-zulassungsstelle-3852901.html)
[^6]: [focus.de](https://www.focus.de/regional/berlin/reisepass-in-berlin-beantragen-das-muessen-sie-beachten_id_6814741.html)
[^7]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlins-innensenator-schlagt-zentralisierung-der-burgeramter-vor-5607997.html#:~:text=Mit%20welchen%20Mitarbeitern%3F-,mit%20welchen%20mitarbeitern,-%3F%22%20Der%20Vorschlag%20des)
[^8]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/der-alltagliche-wahnsinn-an-berliner-burgeramtern-3626182.html#:~:text=ende%202014%20hat%20der%20finanzsenator%20den%20burgeramtern%2031%20zusatzliche%20stellen), [tagesspiegel.de](https://www.tagesspiegel.de/berlin/der-alltagliche-wahnsinn-an-berliner-burgeramtern-3626182.html), [bz-berlin.de](https://www.bz-berlin.de/archiv-artikel/neues-personal-fuer-berlins-buergeraemter), [tagesspiegel.de](https://www.tagesspiegel.de/berlin/senat-verspricht-mehr-als-1200-zusatzliche-stellen-5497792.html)
[^9]: [Wikipedia](https://en.wikipedia.org/wiki/Berlin_population_statistics)
[^10]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/senat-verspricht-mehr-als-1200-zusatzliche-stellen-5497792.html)
[^15]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlin-bekommt-ein-neues-burgeramt-5109592.html#:~:text=pro%20mitarbeiter%20konnen%2018%20termine%20pro%20tag%20angeboten%20werden), [rbb24.de \(archived\)](https://web.archive.org/web/20220104195144/https://www.rbb24.de/politik/beitrag/2021/06/berlin-terminmangel-laengere-oeffnungszeiten-buergeraemter.html)
[^16]: [berlin.de](https://service.berlin.de/terminvereinbarung/hinweise/#:~:text=leider%20werden%20insgesamt%20etwa%201.000%20termine%2Ftag%20nicht%20wahrgenommen.)
[^17]: [tagesspiegel.de](https://www.tagesspiegel.de/berlin/berlins-innensenator-schlagt-zentralisierung-der-burgeramter-vor-5607997.html#:~:text=jeder%20zehnte%20termin%20werde%20dadurch%20in%20pankow%20nicht%20wahrgenommen.%20in%20neukolln%20seien%20es%20sogar%2020%20prozent.)
[^18]: [morgenpost.de](https://www.morgenpost.de/berlin/article213130353/Buergeramt-Berliner-sollen-Wunschtermin-einfacher-bekommen.html#:~:text=das%20neue%20system%20soll%20die%20berliner%20zudem%20per%20e-mail%20oder%20sms)
[^19]: [rbb24.de \(archived\)](https://web.archive.org/web/20211204171454/https://www.rbb24.de/politik/beitrag/2021/07/buergeraemter-berlin-zusaetzliche-termine-massnahmen-.html)
[^20]: [rbb24.de \(archived\)](https://web.archive.org/web/20211101080501/https://www.rbb24.de/politik/beitrag/2021/09/digitalisierung-verwaltung-berlin-r2g-bilanz.html), [tagesspiegel.de](https://www.tagesspiegel.de/berlin/schlange-ade-es-gibt-wieder-termine-im-burgeramt-5915686.html)
[^21]: [berlin.de](https://www.berlin.de/ea/unsere-online-verfahren/service.758896.php)
[^22]: [rbb-online.de \(archived\)](https://web.archive.org/web/20220525072528/https://www.rbb-online.de/supermarkt/zusatzmaterial/2021/aktuell-10-2021/behoerden-buergeramt-ausweis-bezirksamt-online-antraege-berlin-brandenburg.html)
[^23]: [welt.de](https://www.welt.de/regionales/berlin/article144567655/Berliner-verkaufen-Termine-im-Buergeramt-fuer-45-Euro.html)
[^24]: [checkpoint.tagesspiegel.de](https://checkpoint.tagesspiegel.de/langmeldung/1nFaSvn04t1eyLagvxeBL4), [20percent.berlin](https://www.20percent.berlin/p/45-yes-more-corona-changes-trains?s=r), [blog.feather-insurance.com](https://feather-insurance.com/blog/meet-nicolas-from-all-about-berlin/)
[^25]: [allaboutberlin.com](/tools/appointment-finder), [linkedin.com](https://www.linkedin.com/posts/nicolasbouliane_b%C3%BCrgeramt-appointment-finder-activity-6891808142745755648-wsvb?utm_source=linkedin_share&utm_medium=member_desktop_web), [Twitter](https://twitter.com/aboutberlin/status/1485999903327367178)
[^26]: This was a problem in [2015](https://www.tagesspiegel.de/berlin/der-alltagliche-wahnsinn-an-berliner-burgeramtern-3626182.html), [2016](https://www.rbb24.de/politik/wahl/berlin/wahlprogramme/buergeraemter-verwaltung-wahlprogramme-berlin-abgeordnetenhaus-wahl.html), [2017](https://www.tagesspiegel.de/berlin/schlange-ade-es-gibt-wieder-termine-im-burgeramt-5915686.html), [2018](https://www.morgenpost.de/berlin/article213130353/Buergeramt-Berliner-sollen-Wunschtermin-einfacher-bekommen.html), [2019](https://www.tagesspiegel.de/berlin/innensenator-schlagt-alarm-wegen-situation-in-berliner-burgeramtern-6871780.html), [2020](https://www.morgenpost.de/berlin/article230804526/Terminnotstand-in-den-Berliner-Buergeraemtern.html), [2021](https://web.archive.org/web/20220104195144/https://www.rbb24.de/politik/beitrag/2021/06/berlin-terminmangel-laengere-oeffnungszeiten-buergeraemter.html), [2022](https://www.morgenpost.de/berlin/article233456999/buergeramt-berlin-termin-vorzugstermin-tipps-buergeraemter.html) and [2023](https://www.berliner-kurier.de/berlin/keine-online-termine-im-buergeramt-in-sicht-nur-in-diesem-bezirk-haben-sie-noch-chancen-li.308232)
[^11]: [tagesspiegel.de](https://www.tagesspiegel.de/eine-idee-gegen-terminmangel-kunftig-ohne-anmeldung-ins-berliner-burgeramt-10513438.html)