#!/usr/bin/env python

import argparse
from lib.webcrawl import Spider

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--word', help='Find a specific "word" on pages', action='store_true')
    parser.add_argument('-c', '--count', help='Get a count on the most frequently used words', action='store_true')
    parser.add_argument('-l', '--limit', help='Set a limit on pages crawled', action='store_true')
    parser.add_argument('-u', '--url', help='Limit search to pages with a specific "word" in the url', action='store_true')
    parse = parser.parse_args()
    return parse


def main(options):
    word = None
    count = False
    limit = 100
    url = None
    site = raw_input('Enter valid url to begin the crawl: ')
    if options.word:
        word = raw_input('Enter a word to search: ')
    if options.count:
        count = True    
    if options.limit:
        while True:
            try:
                limit = int(raw_input('What limit(must be an integer) do you wish to set?: '))
                break
            except ValueError:
                pass
    if options.url:
        url = raw_input('What word do you want to set the URL\'s to?: ')
    Spider(site, word=word, count=count, limit=limit, url=url)
    return
            

if __name__ == '__main__':
    opts = options()
    main(opts)
