import scrapy
from ..items import JoblistingsItem


class jobListings(scrapy.Spider):
    name = 'Jobs'
    page = 2
    start_urls = {
        'https://www.monsterindia.com/search/software-analyst-jobs?searchId=3e1f034d-eabf-4fe2-b39b-9a37caf97d00/'
    }

    def parse(self, response):
        items = JoblistingsItem()
        abcd = response.css('div.card-apply-content')
        for abc in abcd:
            company_website = abc.css('span.company-name a::attr(href)').extract()
            title = abc.css('.company-name a::text').extract()
            location = abc.css('.col-sm-5 small::text').extract()
            skills = abc.css('.grey-link a::text').extract()
            experience = abc.css('.col-sm-3 small::text').extract()
            salary = abc.css('.col-sm-4 small::text').extract()
            url = abc.css('h3.medium a::attr(href)').extract()

            items['title'] = title
            items['location'] = location
            items['skills'] = skills
            items['experience'] = experience
            items['salary'] = salary
            items['url'] = url
            items['company_website'] = company_website

            yield items

        next_page = 'https://www.monsterindia.com/search/software-analyst-jobs-'+str(jobListings.page)+'?searchId=3e1f034d-eabf-4fe2-b39b-9a37caf97d00'
        jobListings.page += 1
        if jobListings.page <= 100:
            yield response.follow(next_page, callback=self.parse)
