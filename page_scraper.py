# This program uses requests to get data from the MTA turnstile data web pages.
# It then stores that data on a text file on the hard drive
# Modules used

import requests

# These are the MTA turnstile data web page urls from November-December
# The next set of code will scrape data off the web pages of these links

dec14 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191214.txt')
dec7 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191207.txt')
nov30 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191130.txt')
nov23 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191123.txt')
nov16 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191116.txt')
nov9 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191109.txt')
nov2 = requests.get('http://web.mta.info/developers/data/nyct/turnstile/turnstile_191102.txt')


example_var.raise_for_status()      # checks that link is established between program and request destination
                                    # this would be one of the links above

# This second part of code creates a new file, uses a for loop to iterate through the web page's content,
# writes that content onto the new file in chunks, and closes the new file. These files are
# available to see in repository

def scraper(link):
    tsdata = open('NAME_OF_TEXT_FILE.txt', 'wb')    # saves web page to text file in binary
                                                    # "wb" argument used to maintain Unicode encoding of text
    for stuff in link.iter_content(100000):         # method that iterates chunks of web page onto file
        tsdata.write(stuff)                         # the chunks are in bytes data type, 100000 is passed into iter.content()
                                                    # so the files are a good size

    tsdata.close()
    
    return 'Done'

# note that the link parameter in this function has to be one of vars above!

