import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']


    # def parse(self, response):
    #     # using XPath
    #     title = response.xpath('//span[@class="title"]/text()').get()
    #     return {"title": title}

    # Getting Creative
    def parse(self, response):
        return {
            'number': response.xpath('//span[@class="rfc-np"]/text()').get(),
            'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
            # 'title': response.xpath('//span[@class="title"]/text()').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            # 'date': response.xpath('//meta[@name="DC.Date.Issued"]/@content').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'author': response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            # 'author': response.xpath('//span[@class="author-name"]/text()').get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            'headings': response.xpath('//span[@class="subheading"]/text()').getall(),
        }
        


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

