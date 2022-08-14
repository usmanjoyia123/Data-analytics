import scrapy


class QuestionsSpider(scrapy.Spider):
    name = "questions"
    start_urls = [
        'https://datascience.stackexchange.com/'
    ]

    def parse(self, response):
        counter = 0

        for question in response.css('div.question-summary'):

            counter = counter + 1

            summary = question.css("div.summary a.question-hyperlink::text").get()
            votes = question.css("div.cp div.votes div.mini-counts span::text").get()
            views = question.css("div.cp div.views div.mini-counts span::text").get()
            number_of_answers = question.css("div.cp div.status answered div.mini-counts span::text").get()

            print(dict(summary=summary, votes=votes, views=views, number_of_answers=number_of_answers))

            if counter == 10:
                break

from scrapy.crawler import CrawlerProcess
process = CrawlerProcess()
process.crawl(QuestionsSpider)
process.start() # the script will block here until the crawling is finished