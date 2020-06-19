from scrapy import cmdline
cmdline.execute('scrapy crawl house -s LOG_ENABLED=False'.split())