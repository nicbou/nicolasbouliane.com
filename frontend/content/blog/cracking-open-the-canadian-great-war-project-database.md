---
title: Cracking open the Canadian Great War Project database
description: Extracting several hundred megabytes of data from the Canadian Great War Project website.
date_created: 2016-11-16
---

While exploring available data sets for my Great War data project, I found the amazing [Canadian Great War Project](http://www.canadiangreatwarproject.com/) database. It contains a far more refined version of the data found in the [Canadian Expeditionary Force](/blog/parsing-575k-military-records-with-python) dataset, and includes additional information from other sources.

Unfortunately for me, the owner seems to have stopped working on the website, and I was not able to get in touch with him regarding access to the raw data. Fortunately for me, the website was also available as a Windows application *with the database included*. On the downloads page is a 229MB .msi installer for a simple .NET application.

Using [The Unarchiver](http://unarchiver.c3.cx/unarchiver), I extracted the .msi file and retrieved a series of files, one of which was 225.9MB large. When faced with a file without an extension, the best way to know its type is to use the `file` command:

```
file --mime _239D621A339B68AD7601C4A6AEB9CEF8
> _239D621A339B68AD7601C4A6AEB9CEF8: application/vnd.ms-cab-compressed; charset=binary
```

Googling the mimetype gave me the expected file extension (.cab). The Unarchiver effortlessly extracted another series of oddly named files out of the archive.

Once again, a cursory look at the file sizes gave me a good idea of which was the database, but this time, `file` only gave me the `application/octet-stream `mimetype. However, there were several other useful files in there, including the application configuration file with the database connection strings:

```
<connectionStrings>
 ...
 <add name="winCEF.My.MySettings.cefNames2012EConnectionString"
 connectionString="Data Source=|DataDirectory|\cefNames2012E.sdf;Password=...;Persist Security Info=True"
 providerName="Microsoft.SqlServerCe.Client.3.5" />
</connectionStrings>
```

That's all I needed to find the database type (SQL Server CE) as well as the username and password to read it.

The other text files were mostly help pages for the application. They were a treasure trove of information about where the data came from, how to read certain data like rank abbreviations, as well as which information is considered unreliable.

This entire effort turned out to be mostly pointless, as I later found a SQL dump of the database lying in an open directory on the Canadian Great War Project website. In any case, the records will need to be converted from SQL Server to PostgreSQL. This unfortunately involves proprietary software and manual operations, two things that go completely against the goals of this project.

**Update (2016-11-11):** I received a reply from [Jim Kempling](http://acitygoestowar.ca/about/) from the University of Victoria. I am excited to announce that they will take over maintenance of the Canadian Great War Project, and they intend to further organize and normalize the data from the website. This is still fresh information, but I am eager to work with them to get more out of that data set.

## Further reading

This article is part of a series on Canadians at war, a project that aims to link and visualize open data about Canadians in the First World War.

