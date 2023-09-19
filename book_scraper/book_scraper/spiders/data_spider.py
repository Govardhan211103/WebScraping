import scrapy
from book_scraper.items import BookDataItem

class DataSpiderSpider(scrapy.Spider):
    name = "data_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        Books = response.css('article.product_pod')

        for book in Books:
            book_url = book.css('h3 a ::attr(href)').get()

            if "catalogue/" not in book_url:
                book_url_url = "https://books.toscrape.com/catalogue/" + book_url
            else:
                book_url = "https://books.toscrape.com/" + book_url
            
            yield response.follow(book_url, callback = self.parse_printer)


        next_page_url = response.css('li.next a ::attr(href)').get()
        if next_page_url is not None:
            if "catalogue/" not in next_page_url:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page_url
            else:
                next_page_url = "https://books.toscrape.com/" + next_page_url
            
            yield response.follow(next_page_url, callback = self.parse)

        
    # Books.css('h3 a').attrib['title'] - title of book
    # Books.css('.product_price .price_color::text').get() - price
    # Books.css('h3 a').attrib['href'] - link
    # Books = response.css('article.product_pod') - books css text
    # 

    def parse_printer(self, response):

        data_item = BookDataItem()
        data_item['name'] = response.css('h3 a').attrib['title']
        data_item['price'] = response.css('.product_price .price_color::text').get()
        data_item['url'] = response.css('h3 a').attrib['href']
        
        return data_item
