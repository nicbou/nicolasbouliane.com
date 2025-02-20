---
title: How I built currency conversion tooltips
description: This is how I made euro amounts a little easier to understand on All About Berlin.
date_created: 2022-11-24
---

When I'm abroad, I struggle to make sense of amounts in other currencies.

This is also a problem for [All About Berlin](https://allaboutberlin.com/)'s visitors. 40% of them are outside of Germany, and a chunk of the remaining 60% are visitors and recent immigrants.

I wanted to express numbers in currencies that they are familiar with, so **I built an inline currency conversion tooltip**. [See it in action here](https://allaboutberlin.com/guides/german-health-insurance#cost-of-public-health-insurance).

![](/images/currency-conversion-tooltip.png)

{% include "blocks/_tableOfContents.html" %}

## Serving the exchange rates

I get my exchange rates from the [Open Exchange Rate API](https://openexchangerates.org/). Their free plan allows 1,000 API calls per month, or about one call every 45 minutes. I have far more than one visitor every 45 minutes, so I must cache the exchange rates.

I used the same approach as for the Plausible tracking script: proxy the request through All About Berlin's server, and cache the response for a few hours. Calling `allaboutberlin.com/api/exchangerates.json` returns a cached version of `openexchangerates.org/api/latest.json`.

Here's the relevant nginx config:

```
location = /api/exchangerates.json {
    proxy_pass https://openexchangerates.org/api/latest.json?app_id=...;
    proxy_cache jscache;

    # Save valid responses for 6 hours. Serve latest valid response in case of errors.
    proxy_cache_valid 200 6h;
    proxy_cache_use_stale updating error timeout invalid_header http_500;

    # Avoid SSL errors
    proxy_set_header Host openexchangerates.org;
    proxy_ssl_name openexchangerates.org;
    proxy_ssl_server_name on;
    proxy_ssl_session_reuse off;

    # Avoid caching the same page multiple times due to query params or other URL variations
    proxy_cache_key "openexchangerates";
}
```

The displayed exchange rates will be 6 hours old at most. If that's not good enough, you have a [far greater problem](https://en.wikipedia.org/wiki/Hyperinflation). When the cached response is too old, the next request fetches the latest version, and it's cached for another 6 hours.

Proxying external API requests through my server has another benefit: all requests are made to the same domain. This saves DNS query and speeds things up.

This is not a perfect approach, because every page now makes an extra request to get the exchange rates. I wanted to embed the exchange rates in the page before serving it, but exchange rates change faster than my content does. I want to cache a guide until it changes, but update the exchange rates every few hours.

Embedding the exchange rates in the page would also be a problem for The Internet Archive. The old copies of a page should not show old exchange rates.

In the end, an extra request is not such a big deal. It has no perceptible impact, because readers only use those tooltips after a few seconds of reading.

## Building the tooltips

Glossary tooltips were a pain to implement. It's surprisingly hard to build tooltips that open on hover if you have a mouse, and on tap if you have a touch screen.

![](/images/glossary-tooltips.png "Glossary tooltips")

Currency conversion tooltips were easier to build because they behave the same way on all devices. They close when you move your mouse or lift your finger. They don't need to stay open because they don't contain paragraphs of text.

When rendering the content, I wrap euro amounts in a `<span>` tag. `19€` becomes `<span class="currency">19</span>€`. This is done with the `replace` filter in twig.

{% raw %}
```twig
{{ body|replace('/(\\d+(,\\d{3})*(\\.\\d{2})?)€/', '<span class="currency">$1</span>€') }}
```
{% endraw %}

When the page loads, I fetch the exchange rates, format them nicely with [Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat), and set the element's `data-currencies` attribute.

```javascript
fetch('/api/exchangerates.json')
    .then(response => response.json())
    .then(data => {
        document.querySelectorAll('.currency').forEach(el => {
            // Convert from EUR to USD, and from USD to others
            const usdValue = Number(el.textContent.replace(',', '')) / data.rates['EUR'];
            const asCurrency = curr => Intl.NumberFormat('en-US', {style: 'currency', currency: curr}).format(usdValue * data.rates[curr]);
            el.dataset.currencies = `${asCurrency('USD')}\n${asCurrency('CAD')}...`;
        });
    });
```

This is the resulting HTML:

```html
<span class="currency" data-currencies="$4,161\CA$5,555">3,994</span>€
```

Next, I use a bit of CSS to display this information as a tooltip:

```css
.currency[data-currencies]{
    color:inherit!important;
    border-bottom:1px dotted var(--color-border-02);
    cursor:help;
    position:relative;
}
.currency[data-currencies]:hover::after{
    content:attr(data-currencies);
    white-space:pre; /* Only break line on newline characters */
    display:block;
    position:absolute;
    top:var(--line-height);
    left:0;
    z-index:1000;

    font-size:var(--font-size-s);
    line-height:var(--line-height-compact);
    background:var(--color-background-widget);
    padding:var(--spacing-m);
    border-radius:var(--border-radius);
    box-shadow:var(--box-shadow-block);
    border:var(--border-widget);
    text-align:right;
}
```

## Showing the right currencies

Open Exchange Rates lists 169 currencies. I can't show all of them.

![](/images/long-tooltip.png)

I looked at All About Berlin's stats, and ranked my visitors by country. There were a few surprises there: Indian, Polish and Turkish visitors outrank those of a few anglophone countries. Never assume who your visitors are!

![](/images/visitor-distribution.png)

I picked the 5 most popular currencies, but it left out 3 of Germany's neighbours. If I added more currencies, the tooltip became hard to read.

Instead, I check the user's preferred locales in [`navigator.languages`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/languages), and use that to choose which currencies to list. If that doesn't work, I fall back to the hard-coded top 3. I used this technique [again](/projects#anmeldung-form-filler#culture-sniffing) in my Anmeldung form filler.

I used [country-json's data](https://github.com/samayo/country-json/tree/master/src) to make a map of country codes ("US") to currency codes ("USD"). You can [see the code](https://gist.github.com/nicbou/fa67c1a1c48251af1fad0ea018ff9993) for it on Gist. I realised later that the data is wrong, and shows many outdated currencies.

Then, I used that map to show the right currencies:

```javascript
fetch('/api/exchangerates.json')
    .then(...)
    .then(data => {
        ...
        const defaultCurrencyCodes = ["USD", "GBP", "INR", "PLN", "TRY"];
        const countryCodeToCurrencyCode = {"AF":"AFN","AL":"ALL",...};
        const selectedCurrencyCodes = new Set(
            navigator.languages.map(l => countryCodeToCurrencyCode[l.substring(3)]) // en-US -> US
                .filter(Boolean) // Filter out empty country codes
                .concat(defaultCurrencyCodes) // Add the default country codes
        ) // Add to a Set to only keep unique elements

        el.dataset.currencies = Array.from(selectedCurrencyCodes).slice(0, 3).map(c => `${c} ${asCurrency(c)}`).join('\n')
        ...
    });
```

My preferred locales are de-DE, en-UK and fr-CA, so I see British pounds, Canadian dollars, and US dollars as a last default.

## Graceful degradation and other improvements

I often have an unreliable internet connection on the U-Bahn, in hotels, in developing countries, and in Brandenburg. All About Berlin is just text on page, so it should be fully functional as soon as the text is visible on the page. This is why I make such a fuss about making extra requests.

The CSS rules above only apply if the `data-currencies` attributes is set. If the exchange rates have not loaded, the readers just see normal text.

I was also worried about showing outdated exchange rates. This could happen if you are reading an archived version of the page. If it the exchange rates are older than a day, I don't show them.

```javascript
fetch('/api/exchangerates.json')
      .then(...)
      .then(data => {
        const dataAgeInHours = ((new Date(data.timestamp * 1000)).getTime() - Date.now()) / 1000 / 60 / 60;
        if(dataAgeInHours >= 24){
          return;
        }
        ...
      });
```

I also check if the API response is valid, since [fetch does not fail on invalid responses](https://stackoverflow.com/a/40251448).

```javascript
fetch('/api/exchangerates.json')
  .then(response => {
    if(!response.ok){
      throw new Error('Cannot retrieve exchange rates.');
    }
    return response.json()
  })
  .then(...);
```

If the amounts are larger than 100 units of a currency, I don't show cents. I only show the significant digits, to avoid [false precision](https://en.wikipedia.org/wiki/False_precision).

```javascript
const asCurrency = (usdValue, currencyCode) => {
  const value = usdValue * data.rates[currencyCode];
  const showCents = value < 100;
  return Intl.NumberFormat('en-US', {style: 'currency', currency: currencyCode, maximumFractionDigits: showCents ? undefined : 0}).format(value);
};
```

## Bringing it all together

This is the code that made it to production:

```javascript
fetch('/api/exchangerates.json')
      .then(response => {
        if(!response.ok){
          throw new Error('Cannot retrieve exchange rates.');
        }
        return response.json()
      })
      .then(data => {
        const dataAgeInHours = ((new Date(data.timestamp * 1000)).getTime() - Date.now()) / 1000 / 60 / 60;
        if(dataAgeInHours >= 24){
          return;
        }
        const defaultCurrencyCodes = ["USD", "GBP", "INR"];
        const countryCodeToCurrencyCode = {"AF":"AFN","AL":"ALL","DZ":"DZD","AS":"USD","AO":"AOA","AI":"XCD","AQ":"XCD","AG":"XCD","AR":"ARS","AM":"AMD","AW":"AWG","AU":"AUD","AZ":"AZN","BS":"BSD","BH":"BHD","BD":"BDT","BB":"BBD","BZ":"BZD","BJ":"XOF","BM":"BMD","BT":"BTN","BO":"BOB","BA":"BAM","BW":"BWP","BV":"NOK","BR":"BRL","IO":"USD","BN":"BND","BG":"BGN","BF":"XOF","BI":"BIF","KH":"KHR","CM":"XAF","CA":"CAD","CV":"CVE","KY":"KYD","CF":"XAF","TD":"XAF","CL":"CLP","CN":"CNY","CX":"AUD","CC":"AUD","CO":"COP","KM":"KMF","CG":"XAF","CK":"NZD","CR":"CRC","HR":"HRK","CU":"CUP","CZ":"CZK","DK":"DKK","DJ":"DJF","DM":"XCD","DO":"DOP","TP":"USD","EG":"EGP","SV":"SVC","GQ":"XAF","ER":"ERN","ET":"ETB","FK":"FKP","FO":"DKK","FJ":"FJD","PF":"XPF","GA":"XAF","GM":"GMD","GE":"GEL","GH":"GHS","GI":"GIP","GL":"DKK","GD":"XCD","GU":"USD","GN":"GNF","GY":"GYD","HT":"HTG","HM":"AUD","HN":"HNL","HK":"HKD","HU":"HUF","IS":"ISK","IN":"INR","ID":"IDR","IR":"IRR","IQ":"IQD","IL":"ILS","CI":"XOF","JM":"JMD","JP":"JPY","JO":"JOD","KZ":"KZT","KE":"KES","KI":"AUD","KW":"KWD","KG":"KGS","LA":"LAK","LB":"LBP","LS":"LSL","LR":"LRD","LY":"LYD","LI":"CHF","MK":"MKD","MW":"MWK","MY":"MYR","MV":"MVR","ML":"XOF","MH":"USD","MU":"MUR","MX":"MXN","FM":"USD","MD":"MDL","MN":"MNT","MS":"XCD","MA":"MAD","MZ":"MZN","NA":"NAD","NR":"AUD","NP":"NPR","AN":"ANG","NC":"XPF","NZ":"NZD","NI":"NIO","NE":"XOF","NG":"NGN","NU":"NZD","NF":"AUD","KP":"KPW","GB":"GBP","MP":"USD","NO":"NOK","OM":"OMR","PK":"PKR","PW":"USD","PA":"PAB","PG":"PGK","PY":"PYG","PE":"PEN","PH":"PHP","PL":"PLN","PR":"USD","QA":"QAR","RO":"RON","RU":"RUB","RW":"RWF","SH":"SHP","KN":"XCD","LC":"XCD","VC":"XCD","WS":"WST","ST":"STD","SA":"SAR","SN":"XOF","RS":"RSD","SC":"SCR","SL":"SLL","SG":"SGD","SB":"SBD","SO":"SOS","ZA":"ZAR","GS":"GBP","KR":"KRW","SS":"SSP","LK":"LKR","SD":"SDG","SR":"SRD","SJ":"NOK","SZ":"SZL","SE":"SEK","CH":"CHF","SY":"SYP","TJ":"TJS","TZ":"TZS","TH":"THB","CD":"CDF","TG":"XOF","TK":"NZD","TO":"TOP","TT":"TTD","TN":"TND","TR":"TRY","TM":"TMT","TC":"USD","TV":"AUD","UG":"UGX","UA":"UAH","AE":"AED","UK":"GBP","US":"USD","UM":"USD","UY":"UYU","UZ":"UZS","VU":"VUV","VN":"VND","VG":"USD","VI":"USD","WF":"XPF","EH":"MAD","YE":"YER","ZM":"ZMW"};
        const selectedCurrencyCodes = new Set(
          navigator.languages.map(l => countryCodeToCurrencyCode[l.substring(3)])
            .filter(Boolean)
            .concat(defaultCurrencyCodes)
        );
        const asCurrency = (usdValue, currencyCode) => {
          const value = usdValue * data.rates[currencyCode];
          const showCents = value < 100;
          return Intl.NumberFormat('en-US', {style: 'currency', currency: currencyCode, maximumFractionDigits: showCents ? undefined : 0}).format(value);
        };

        document.querySelectorAll('.currency').forEach(el => {
          const usdValue = Number(el.textContent.replace(',', '')) / data.rates['EUR'];
          el.dataset.currencies = Array.from(selectedCurrencyCodes).slice(0, 3).map(code => asCurrency(usdValue, code)).join('\n')
        });
      });
```

