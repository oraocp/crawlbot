# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示lxml解析HTML内容
# 创建日期：2018/1/24
# -------------------------------------------------------------------------

import re
from lxml.html import fromstring
from pegasus.crawlbot.chap01.common import download


def scrape(html):
    tree = fromstring(html)
    td = tree.cssselect('tr#places_neighbours__row > td.w2p_fw')[0]
    area = td.text_content()
    return area

if __name__ == '__main__':
    html = download("http://example.webscraping.com/view/United-Kingdom-239'")
    print(scrape(html))
