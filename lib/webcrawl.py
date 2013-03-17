#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from collections import Counter
import requests
import re


class Spider(object):
    
    def __init__(self, site, **kwargs):
        self.site = site
        wrdpg = []
        try:
            data, soup = self.crawl(self.site)
        except TypeError:
            print 'Bad Url -- check the address to make sure its correct'
            return
        if not data:
            print 'Bad Url -- check the address to make sure its correct'
            return
        if kwargs['word'] and kwargs['word'] in data:
            wrdpg.append(self.site)
        if kwargs['url']:
            urls = [i.get('href') for i in soup.findAll('a') if kwargs['url'] 
                    in str(i.get('href')) and 'http' in str(i.get('href'))] 
        else:
            urls = [i.get('href') for i in soup.findAll('a') if 'http' in
                    str(i.get('href'))]
        if len(urls) >= kwargs['limit']:
            if not kwargs['word'] and not kwargs['count']:
                for i in urls[:kwargs['limit']]:
                    print i            
            else:
                for i in urls[:kwargs['limit']]:
                    try:
                        new_data, soup = self.crawl(str(i))
                        if new_data:
                            if kwargs['word'] and kwargs['word'] in new_data:
                                wrdpg.append(i)
                            data = data + new_data
                    except (TypeError, UnicodeEncodeError) as e:
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
                            urls = urls + [i.get('href') for i in soup.findAll('a')
                                           if kwargs['url'] in str(i.get('href'))
                                           and 'http' in str(i.get('href'))]
                        else:
                            urls = urls + [i.get('href') for i in soup.findAll('a')
                                           if 'http' in str(i.get('href'))]
                    if new_data:
                        if kwargs['word'] and kwargs['word'] in new_data:
                            wrdpg.append(urls[pos])
                        data = data + new_data
                except TypeError:
                    pass
                except IndexError:
                    print 'Sorry no Url\'s'
                    return
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
