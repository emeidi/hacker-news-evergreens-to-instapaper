hacker-news-evergreens-to-instapaper
====================================

Submits all YCombinator Hacker News articles considered "evergreens" to Instapaper for further reading

Motivation
----------
In November 2014, Ben Autrey calculated a list of YCombinator Hacker News "evergreen" stories and published it on his blog:

https://contextly.com/blog/2014/11/hacker-news-evergreen-stories-ordered-score/

Unfortunately, he was not able to link directly to the articles itself, but only to the Hacker News pages with the commentaries for each and every story.

I therefore programmed a few loosely coupled scripts to ...

1. download the aforementioned blog article
1. extract all Hacker News URLs
1. cache all Hacker News pages
1. traverse all pages and extracting the article links
1. send the article links to my Instapaper Pro account for further reading

In this repository, you will find scripts and raw text files to also submit the articles to your Instapaper account:

* If you're just interested in the list of direct links to the articles, have a look at `urls-articles.txt`.
* If you'd like to submit those URLs to your Instapaper account, please start `submit-to-instapaper.py` after inserting your credentials into the script