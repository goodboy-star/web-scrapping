import scrapy


class ScrappingSpider(scrapy.Spider):
    name = "scrapping"

    start_urls = ["https://quotes.toscrape.com"]

    def parse_author(self, response):
        for quote in response.css("div.author_details"):
            yield {
                "name": quote.css("h3.author-title::text").get(),
                "birthdate": quote.css(".author-born-date::text").get(),
                "bio": quote.css(".author-description::text").get(),
            }

        # pd.read_json('./result.jsonl').to_excel("output.xlsx")
        about_page = response.css(".author + a")
        # if about_page is not None:
        print("11111111111111111", about_page, "----------------------")
        # about_page = response.urljoin(about_page)
        # yield scrapy.Request(about_page, callback=self.parse_author)
