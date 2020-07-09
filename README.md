# web-scraping-using-scrapy
Here, Crawling the jobs data from Monster website is done using scrapy.

You can scrap any webpage using this code by replacing the url of the webpage in the code and also the corresponding path in the css.You can find the path by inspecting the source webpage.

To execute,enter into the working directory and type the below command:

I had given the name of my spider as Jobs.Replace it with the name you have given to the spider while executing the below commands.

To get output in the current terminal
--> scrapy crawl Jobs

To get output in csv file
--> scrapy crawl Jobs -o filename.csv

To get output in json file
--> scrapy crawl Jobs -o filename.json
