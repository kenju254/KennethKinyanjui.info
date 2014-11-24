Title: Changing Wordpress URLs Manually on Your VPS
Date: 21-11-2014
Tags: Wordpress, DigitalOcean, VPS
Category: Technology
Slug: changing-urls-manually-in-wordpress
Author: Kenneth Kinyanjui

## Introduction

Have you been in a situation where you are about to launch your webiste and at the 11th hour something happens that just spoils everything and you are like What the Heck!!!!!

## The Problem
Well about a month ago , I was having my WTF moment and I was able to solve it , silently without anyone noticing. So yesterday , I had a problem with Permalinks on a Wordpress site we are building for a client. So when resolving to clean urls for the site I was getting this nasty error and I wasn't pleased at all.


My co worker and I sorted to solving the problem and now as we were doing some stuff on the WP-Dashboard , we slightly changed the SiteURL and SiteName and shit suddenly we couldn't access the Dashboard and the site was not working.

## Thinking of a Solution
The only access I had was ssh to where we had hosted the site. So this is one nasty situation I was in and clearly didn't know how to surpass it . Quickly, we knew what has happended we had messed with the siteurl and sitename , so the only option was changing it manually.

## Getting Down To Business

So Clearly, the SiteUrl and SiteName are stored in the wordpress database under the wp_options. So i knew I had to change it manually and by having ssh access and also access to the databases then that was not going to be a problem.

So I sorted to do the following

### Get the current sitename

Hop on to your VPS and access your mysql.

I take it that you already know how to access your mysql shell. The first thing is gett ing to know the value of the Sitename that is on the database.


```
username@[~/Desktop]: mysql -u root -p databasename
Enter password:
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor. Commands end with ; or g.
Your MySQL connection id is 892
Server version: 5.5.13 MySQL Community Server (GPL)

Copyright (c) 2000, 2010, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or 'h' for help. Type 'c' to clear the current input statement.

mysql> UPDATE wp_options SET option_value = replace(option_value, 'http://www.oldurl', 'http://www.newurl') WHERE option_name = 'home' OR option_name = 'siteurl';
Query OK, 0 rows affected (0.00 sec)
Rows matched: 2 Changed: 0 Warnings: 0

mysql> UPDATE wp_posts SET guid = replace(guid, 'http://www.oldurl','http://www.newurl');
Query OK, 0 rows affected (0.02 sec)
Rows matched: 964 Changed: 0 Warnings: 0

mysql> UPDATE wp_posts SET post_content = replace(post_content, 'http://www.oldurl', 'http://www.newurl');
Query OK, 0 rows affected (0.05 sec)
Rows matched: 964 Changed: 0 Warnings: 0

mysql> UPDATE wp_postmeta SET meta_value = replace(meta_value,'http://www.oldurl','http://www.newurl');g
Query OK, 0 rows affected (0.01 sec)
Rows matched: 686 Changed: 0 Warnings: 0
```
