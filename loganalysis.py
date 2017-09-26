#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Log Analysis Program

from loganalysis_db import get_top_three_articles, get_top_authors, \
    get_high_http_error_date
from datetime import datetime


def displayMostPopularArticles():
    """
    display three most popular articles
             presented as descending sorted list
             e.g. "Princess Shellfish Marries Prince Handsome" — 1201 views
    """
    print "What are the most popular three articles of all time?"
    articles = get_top_three_articles()
    for title, views in articles:
        print " \"{}\" - {} views".format(title, views)
    print "\n"


def displayMostPopularAuthors():
    """
    display most popular authors
             presented as sorted list
             e.g. Ursula La Multa — 2304 views
    """
    print "Who are the most popular article authors of all time?"
    authors = get_top_authors()
    for author, views in authors:
        print " {} - {} views".format(author, views)
    print "\n"


def displayDaysOfOnePercentError():
    """
    display the date where more than 1% of http code returned error
             e.g. July 29, 2016 — 2.5% errors
    """
    print "On which days did more than 1% of requests lead to errors? "
    dates = get_high_http_error_date()
    for d in dates:
        if d is not None:
            print('{0:%B %d, %Y} - {1:.1f}% errors'.format(d[3], d[2]))
    print "\n"

if __name__ == '__main__':
    displayMostPopularArticles()
    displayMostPopularAuthors()
    displayDaysOfOnePercentError()
    print "Success! "
