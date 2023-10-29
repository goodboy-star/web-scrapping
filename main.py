import scrapy
# import pandas as pd
import AuthorSpider


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

    # def parse_author(self, response):
    #     for quote_t in response.css("div.author_details"):
    #         yield {
    #             "name": quote_t.css("h3.author-title::text").get(),
    #             "birthdate": quote_t.css(".author-born-date::text").get(),
    #             "bio": quote_t.css(".author-description::text").get(),
    #         }

        # pd.read_json('./result.jsonl').to_excel("output.xlsx")
        # about_page = response.css("span a::attr(href)").get()
        # if about_page is not None:
        #     about_page = response.urljoin(about_page)
        #     yield scrapy.Request(about_page, callback=self.parse_author)
