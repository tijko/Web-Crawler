#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from collections import Counter
import requests
import re


class Spider(object):
    
    def __init__(self, site, **kwargs):
        self.site = site
        wrdpg = []
        urls = []
        try:
            data, soup = self.crawl(self.site)
        except TypeError:
            print 'Bad Url -- check the address to make sure its correct(include http://)'
            return
        if not data:
            print 'Bad Url -- check the address to make sure its correct'
            return
        if kwargs['word'] and kwargs['word'] in data:
            wrdpg.append(self.site)
        if kwargs['url']:
            urls = [i.get('href') for i in soup.findAll('a')
                    if i.get('href') is not None and 
                    kwargs['url'] in i.get('href') and 
                    'http' in i.get('href')] 
        if kwargs['skip']:
            if urls:
                urls = [i for i in urls if kwargs['skip'] not in i]
            else:
                urls = [i.get('href').encode('utf-8') for i in soup.findAll('a') 
                        if i.get('href') is not None and 
                        'http' in i.get('href') and
                        kwargs['skip'] in i.get('href')]
        if not kwargs['url'] and not kwargs['skip']:
            urls = [i.get('href') for i in soup.findAll('a') 
                    if i.get('href') is not None and
                    'http' in i.get('href')]
        urls = [i for i in set(urls)]
        if len(urls) >= kwargs['limit']:
            if not kwargs['word'] and not kwargs['count']:
                for i in urls[:kwargs['limit']]:
                    print i            
            else:
                for i in urls[:kwargs['limit']]:
                    try:
                        new_data, soup = self.crawl(i)
                        if new_data:
                            if kwargs['word'] and kwargs['word'] in new_data:
                                wrdpg.append(i)
                            data = data + new_data
                    except TypeError:
                        pass 
            if kwargs['word']:
                for i in urls[:kwargs['limit']]:
                    print i
                print '\nFound %s on:' % kwargs['word']
                for i in wrdpg:
                    print i
            if kwargs['count']:
                print Counter(data)
            return
        else:
            pos = 0
            while len(urls) < kwargs['limit']:
                try:
                    new_data, soup = self.crawl(urls[pos])
                    if soup:
                        if kwargs['url']:
                            urls = urls + [i.get('href').encode('utf-8') for i in soup.findAll('a')
                                           if i.get('href') is not None and
                                           kwargs['url'] in i.get('href')
                                           and 'http' in i.get('href')]
                        if kwargs['skip']:
                            urls = [i for i in urls if kwargs['skip'] not in i]
                            urls = urls + [i.get('href').encode('utf-8') for i in soup.findAll('a')
                                           if i.get('href') is not None and
                                           kwargs['skip'] not in i.get('href') and
                                           'http' in i.get('href')]
                        if not kwargs['url'] and kwargs['skip']:
                            urls = urls + [i.get('href').encode('utf-8') for i in soup.findAll('a')
                                           if i.get('href') is not None and
                                           'http' in i.get('href')]
                    if new_data:
                        if kwargs['word'] and kwargs['word'] in new_data:
                            wrdpg.append(urls[pos])
                        data = data + new_data
                except TypeError:
                    pass
                except IndexError:
                    if urls:
                        for i in urls:
                            print i
                        return
                    print 'Sorry no Url\'s'
                    return
                urls = [i for i in set(urls)]
                pos += 1
        if not kwargs['word'] and not kwargs['count']:
            for i in urls[:kwargs['limit']]:
                print i
        if kwargs['word']:
            for i in urls[:kwargs['limit']]:
                print i
            print '\nFound %s on:' % kwargs['word']
            for i in wrdpg:
                print i
        if kwargs['count']:
            print Counter(data)
        return


    def crawl(self, page):
        try:
            req = requests.get(page)
            soup = BeautifulSoup(req.content)
            data = re.sub(r'[^a-zA-Z]', ' ', soup.text)
            data = [i for i in data.split(' ') if i != '']
            return data, soup
        except (requests.exceptions.ConnectionError,
                requests.exceptions.InvalidURL,
                requests.exceptions.MissingSchema,
                AttributeError) as e:
            pass
