# Web-Crawler

This is a basic web-crawler that can also query the page data of each address.  Using 
commandline arguments you can narrow search down or return a couple of extra stats.

#### Set-up

The Web-Crawler uses a couple of modules not included in python's standard library, so
you will need to get those installed first if you don't already have them.

You can:

    pip install requests

And:

    pip install BeautifulSoup

Once you get those, you're ready to go.

#### Usage 

A small example of Web-Crawler.

Run the following from your commandline:

    python main.py -h

Which will print out the options available:

    usage: main.py [-h] [-w] [-c] [-l] [-u]

    optional arguments:
      -h, --help   show this help message and exit
      -w, --word   Find a specific "word" on pages
      -c, --count  Get a count on the most frequently used words
      -l, --limit  Set a limit on pages crawled
      -u, --url    Limit search to pages with a specific "word" in the url

You can put a couple of options together:

    python main.py -lu
    Enter valid url to begin the crawl: http://www.foobar.com
    What limit(must be an integer) do you wish to set?: 10
    What word do you want to set the URL's to?: politics
    
