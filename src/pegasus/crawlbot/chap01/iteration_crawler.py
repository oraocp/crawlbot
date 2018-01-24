# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：
# 创建日期：2018/1/22
# -------------------------------------------------------------------------

import itertools
import re

from .common import download


def crawl_sitemap(url):
    """
    通过网站地图来抓取网站
    :param url: 网站地图的URL地址
    """
    # 下载sitemap文件
    sitemap = download(url)
    # 从sitemap中解析出链接
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # 下载这些链接
    for link in links:
        html = download(link)
        # scape html here
        # ...


def iteration():
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-{}'.format(page)
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum amount of errors in a row so exit
                break
                # so assume have reached the last country ID and can stop downloading
        else:
            # success - can scrape the result
            # ...
            num_errors = 0
