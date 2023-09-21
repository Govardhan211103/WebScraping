import scrapy
from book_scraper.items import BookDataItem

class DataSpiderSpider(scrapy.Spider):
    name = "data_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    custom_settings = {
        'FEEDS': {
            'scraped_data.json': {'format': 'json', 'overwrite': True},
        }
    }

    def parse(self, response):
        Books = response.css('article.product_pod')

        for book in Books:
            book_url = book.css('h3 a ::attr(href)').get()
            if 'catalogue/' in book_url:
                updated_book_url = 'https://books.toscrape.com/' + book_url
            else:
                updated_book_url = 'https://books.toscrape.com/catalogue/' + book_url
            yield response.follow(updated_book_url, callback=self.parse_attributes)

        next_page_url = response.css('li.next a ::attr(href)').get()
        if next_page_url is not None:
            if "catalogue/" not in next_page_url:
                updated_next_page_url = "https://books.toscrape.com/catalogue/" + next_page_url
            else:
                updated_next_page_url = "https://books.toscrape.com/" + next_page_url
            
            yield response.follow(updated_next_page_url, callback = self.parse)


    def parse_attributes(self, response):

        data_item = BookDataItem()
        table_rows = response.css("table tr")
    
        data_item['url'] = response.url,
        data_item['title'] = response.css('.product_main h1::text').get(),
        data_item['upc'] = table_rows[0].css("td ::text").get()
        data_item['product_type' ] = table_rows[1].css("td ::text").get(),
        data_item['price_excl_tax'] = table_rows[2].css("td ::text").get(),
        data_item['price_incl_tax'] = table_rows[3].css("td ::text").get(),
        data_item['tax'] = table_rows[4].css("td ::text").get(),
        data_item['availability'] = table_rows[5].css("td ::text").get(),
        data_item['num_reviews']=  table_rows[6].css("td ::text").get(),
        data_item['stars'] = response.css("p.star-rating").attrib['class'],
        data_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        data_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        data_item['price'] = response.css('p.price_color ::text').get(),
    
        yield data_item
