---
title: How to fix `failed to connect to host` with GitHub webhooks
description:
date_created: 2025-10-14
categories:
---
I use `webhook` and Github webhooks to redeploy All About Berlin when I push new changes. I'm using [`adnanh/webhook`](https://github.com/adnanh/webhook) on an Ubuntu 24.04 VPS on DigitalOcean, behind CloudFlare.
## The problem

The webhooks failed with the following message: **"We couldn't deliver this payload: failed to connect to host."**

Let's look at the facts:

- The `webhook` server ran properly on port 9000.  I started it with `webhook -port 9000 -hooks /etc/webhook/hooks.yml -template -verbose`
	- I started `webhook` with `systemd`. `systemctl status webhook` showed that the service was running fine.
	- It ran properly. I saw it when I ran  `ps ax|grep webhook`.
	- It replied correctly. When I ran `curl http://[server IP]:9000/hooks/my-hook`, it returned a response: `Hook rules were not satisfied`.
- Port 9000 was closed
	- Github webhooks failed because they could not reach the server on that port. The error was `failed to connect to host`.
	- My local machine could not reach the server on that port either. The port was closed.
		- `nc -zv [server IP] 9000` returned `connect to [server IP] port 9000 from [...] failed: Operation timed out`
		- `curl http://[server IP]:9000/hooks/my-hook` failed with `curl: (28) Failed to connect to [server IP] port 9000 after 75003 ms: Couldn't connect to server`
- CloudFlare was not the problem. I was bypassing it by using the server's IP address.
- DigitalOcean's firewall was not the problem. There were no firewalls in my dashboard.
- That left one possible culprit: **the server's firewall was blocking port 9000**. Running `tail -n100 /var/log/ufw.log | grep 9000` on the server showed my attempts to connect on port 9000: `2025-10-... [UFW BLOCK] IN=eth0 ... SRC=[my IP] DST=[server IP] ... DPT=9000 ...`
## The solution

**Unblock port 9000 in ufw.** I ran `ufw allow 9000/tcp && ufw reload`. Now the port is reachable and `webhook` works as expected.

Now the webhook `http://[server IP]:9000/hooks/deploy` works, but `http://allaboutberlin.com:9000/hooks/deploy` still fails, still with `Operation timed out` (curl) and `failed to connect to host` (GitHub webhooks).

This is because **CloudFlare is blocking port 9000**, and all ports that are not in [this list](https://developers.cloudflare.com/fundamentals/reference/network-ports/). At that point, there are two workarounds:
- Use one of the [HTTP ports supported by CloudFlare](https://developers.cloudflare.com/fundamentals/reference/network-ports/#network-ports-compatible-with-cloudflares-proxy) - this is what I did. I chose port 8080, and the webhook is now at `http://allaboutberlin.com:8080/hooks/deploy`.
- Bypass CloudFlare and use the server's IP address directly, and use `http://[server IP]:9000/hooks/deploy` as the webhook URL. This could break a long time in the future, when you forgot everything about webhooks, or someone else is responsible for this project. Not recommended.

If you choose the port 8080 route, remember to delete the `ufw` rule you have just added. `ufw status numbered` to find the rule number, and `ufw delete [rule number] && ufw reload` to delete the rule and apply changes.