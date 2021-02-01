import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']


    def parse(self, response):
        # using XPath
        title = response.xpath('//span[@class="title"]/text()').get()
        return {"title": title}
        


# this parse functions is passed a response object by scrapy
# we want to fill this in with something that will return an object
# containing the data scraped from our site
# essentially this turns a response object into a 
# parsed Python dictionary of data. When looking at the page source
# we see that the title is demarcated by <span class="title">
# there are two main ways to capture this title string with scrapy
# using XPath selectors or using CSS selectors
# using css: # title = response.css('span.title::text').get() 
# if we want a list we can use getall()
# Then, we want to return a python dictionary containing this title data
# run spider using scrapy command in terminal
# scrapy runspider ietf.py
# we should see a lot of data including our title
# {'title': 'A Standard for the Transmission of IP Datagrams on Avian Carriers'}
# now we knoiw our spider works!

