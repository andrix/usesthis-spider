Usesthis
========

Scrapy spider to get the interviews from The Setup : http://usesthis.com.
The intention is to create some stats on Hardware / Software from the interviews,
to be able to trends some products.

Usage
=====

To output a json file:

:: 
    scrapy crawl usesthis.com --set FEED_URI=usesthis.json --set FEED_FORMAT=json

Dependencies
============

* Scrapy 0.12 - http://scrapy.org



