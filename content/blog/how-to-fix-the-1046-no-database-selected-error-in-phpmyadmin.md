---
title: How to fix the "#1046: No database selected" error in phpMyAdmin
description: Are you getting this error when importing a .sql file in phpMyAdmin? Here's how you can solve it.
date_created: 2013-04-04
---

Here is a simple solution to the "#1046: No database selected" error when trying to import a .sql file in phpMyAdmin.

## Solution #1: Before importing

In phpMyAdmin, click on the Export tab **from the home page** of phpMyAdmin, without selecting any database. phpMyAdmin will then include instructions to create and select the database when you import it.

This solution does not apply to most shared hosts, since they won't allow you to create a database from phpMyAdmin.

## Solution #2: The alternative fix

Unlike solution #1, this one also works on shared hosts.

- Create the new database on your server, then write down the name.
- Open your .sql file with a text editor
- Insert the following line right before the first `CREATE TABLE` instruction in your .sql file: `USE your_database_name_here;`
- Save your file, then import it in phpMyAdmin.

