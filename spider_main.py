# -*- coding:utf-8 -*-
from wenku_spider import html_paser, html_output, html_downloader, url_manager
from urllib.parse import quote


class SpiderMain(object):
    def __init__(self):
        self.urlm = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 网页下载器
        self.parser = html_paser.HtmlPaser()  # html解析器
        self.output = html_output.HtmlOutput()  # 爬虫爬取数据输出成html文件

    def craw(self, root_url):
        count = 1
        self.urlm.add_new_url(root_url)
        urls = self.urlm.get_new_urls(root_url, 10)
        self.urlm.add_new_urls(urls)
        while self.urlm.has_new_url():
            try:
                new_url = self.urlm.get_new_url()
                print('正在爬取第 %d 页:%s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(new_url, html_cont)
                self.output.collect_data(new_data)
                if count == 1000:
                    break
                count += 1

            except:
                print('爬取错误')
        self.output.output_html()


if __name__ == "__main__":
    root_url = "https://wenku.baidu.com/search?word="
    keywords = quote('简历') #对中文进行gb2312编码
    root_url += keywords
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
