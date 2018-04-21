Title: Python to the rescue!
Date: 2018-04-12 9:30
Lang: en
Tags: python, backup, macos, server, dropbox
Category: Programming
Slug: python_to_the_rescue
Author: Victor Domingos
Cover: images/2018/npk-backup.png
Summary: One day you find yourself in a situation you need to set up an automatic backup system and you realise that your old server does not support Dropbox anymore. The sollution: getting your hands to work and write a program for that task.

## The problem
In the middle of some corporate changes, my company had the need to relocate an old Mac mini server, which was responsible for one of its most important databases. It was a custom-made application based on Filemaker - a very old version of Filemaker running on Mac OS 10.6 Snow Leopard. Nobody seemed to be aware that there wasn't anymore a backup strategy in place. Until one night, when there was a big assault and lots of computers got stolen. Being a headless mini computer certainly helped that Mac to remain intact. But if it had been stolen, there would be a big loss in data that was essential for the company's business. 

So, suddently it was very clear that there was an urgent need to put back in place a backup strategy which had to include an off-site copy for the database. Someone came up with the idea of using a Dropbox account as an inexpensive and very simple to implement option, to be complemented with other forms of backup. It was pretty straightforward: just configuring Filemaker to save its backup files into a folder that was monitored and synced by the Dropbox utility. Except for one little thing... Dropbox wasn't officially supported on such an old operating system anymore. 

It was a very stable machine and probably upgrading the operating system would break compatibility with the old version of Filemaker. And buying a new Filemaker license was certainly an expensive option that the administration wouldn't be very fond of. 

## Python to the rescue!

Fortunately, it ended up being pretty simple to solve with some lines of Python code. Dropbox has a nice API that is also available as a Python package. The [NPK-Backup](http://bit.ly/NPK-Backup) script was written to be used in that context, as a Launch Daemon running everyday at predefined times. It periodically zips and uploads to Dropbox any new folders available inside the local Filemaker backup folder. Then, in a separate machine, just for convenience, another script is used to remove the older files, ensuring that the Dropbox account does not get over its storage quota.

It's not a very elaborate, and it certainly isn't a perfect backup system. But it solved that specific problem with virtually no costs (just took a few spare hours to write and test the script) and in a practical way. 
