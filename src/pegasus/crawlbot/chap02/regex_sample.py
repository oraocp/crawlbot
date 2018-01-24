# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示使用正则表达式解析页面内容
# 创建日期：2018/1/24
# -------------------------------------------------------------------------

import re

from pegasus.crawlbot.chap01.common import download


def scrape(html):
    result = re.findall('script.*? src href="(.*?)"', html)
    if result:
        return result
    else:
        return "Find no 'area' input"


if __name__ == '__main__':
    html = download('http://www.163.com')
    print(html)
    css_list = scrape(html)
    if css_list:
       for css in css_list:
           print(css)
