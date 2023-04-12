---
title: What is Cross-Site Request Forgery (CSRF)?
description: 
date_created: 2014-04-24
---

Following the previous "you should know" introductions about [SQL injection](http://wisercoder.com/sql-injection/) and [XSS injection](http://wisercoder.com/xss-injection/), here is a short introduction to CSRF. I'll quickly define it with a few examples, then provide solutions to avoid it.

CSRF (or XSRF) is an exploit where a malicious application transmits unsolicited requests to another web application in the name of an unsuspecting user.

For example, a malicious website could exploit on your application by putting an image with `http://yourapp.com/transferCredits?amount=1500&to=hacker` as the source on the page. If an unsuspecting visitor loads the image and is also connected to yourapp.com, he would unknowingly transfer 1500 credits to the hacker.

```
<p>
 This image on maliciouswebsite.com would silently
 delete a connected user's account on importantsite.com
 <img src="http://importantsite.com/api/account/delete">
</p>
```

Click jacking is a similar exploit. A malicious website could move an invisible Like button right under your mouse as you are about to click, making you Like a Facebook page without your consent.

Unlike XSS and SQL injections, you might not notice when a CSRF attack takes place, since it will look as a legitimate request.

**Preventing CSRF**

Using POST for requests with side-effects (creating, updating or deleting records) instead of GET will already help make your application safer.

To prevent CSRF, you need to verify that the request comes from a legitimate user. This can be achieved by emitting a unique token when serving the page that would normally call an action. When you receive a request, you verify that a valid token was supplied with that request. This is the approach most frameworks take.

Alternatively, you can verify the `Origin` and `Referer` headers to make sure that the request comes from your own site.

If you use Django, you are required by default to use CSRF tokens for POST requests with side-effects.

As usual, OWASP has [an excellent guide](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29_Prevention_Cheat_Sheet) about preventing CSRF.

