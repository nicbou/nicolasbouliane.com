---
title: How to fix HP scanning errors in MacOS
description: What to do when your HP scanner won't connect to your Mac.
date_created: 2019-04-10
---

If you made the mistake of buying an HP printer, you might encounter one of the following problems:

- The scanner does not work. Both HP Easy Scan and the OSX Printers and Scanners utilities fail. Printing might still work.
- In HP Easy Scan, you get a message that says *Scanner reported an error: An error occurred while communicating with the scanner*
- In the OSX Printers and Scanners utility, you get a message that says *An error occurred while communicating with the scanner. (-9923)*

I had this problem with my HP M28w multifunction printer. The HP support forums were useless, but I managed to fix it.

The following things did **not** work:

- Rebooting the printer
- Restarting HP Easy Scan
- [Resetting the print system](https://support.hp.com/bg-en/document/c04889653)

One of these things fixed scanning for me:

1. Disable IPv6 on the printer. You can do this by opening HP Utility. In *Network > IPv6*, deactivate IPv6 and save the settings. It did not seem to fix my issue, but [it worked for many other users](https://toggen.com.au/blog/it-tips/macos-sierra-scanning-fail).
2. Run [HP Easy Start](https://support.hp.com/us-en/drivers/printers) again and reinstall everything. When I did this, I got a message that said *System Extension cannot be used: The system extension “/Library/Extensions/hp_fax_io.kext” was installed improperly and cannot be used. Please try reinstalling it, or contact the product’s vendor for an update*. I simply deleted that file. The printer started working again.

![](/images/hp-scanner-error.png)

![](/images/hp-utility-ipv6.png)

