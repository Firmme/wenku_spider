# -*- coding:utf-8 -*-
from urllib import request



class HtmlDownloader(object):
    """
    如果无法正常打开第一个网页,程序将出错
    """
    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read().decode('gb2312','ignore')

