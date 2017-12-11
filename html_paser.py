# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re


class HtmlPaser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
        new_data = self._get_new_data(soup)

        return new_data

    def _get_new_data(self, soup):
        res_data = {}
        links = soup.find_all('a', href=re.compile(r"/view/\w+.html"))
        links = soup.find_all('a', title=re.compile(r"\S"))
        for link in links:
            wenku_url = link['href']
            title = link['title']
            print(title)
            res_data[wenku_url] = title
        return res_data
