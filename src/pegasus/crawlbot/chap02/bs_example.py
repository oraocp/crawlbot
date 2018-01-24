# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示使用BeautifulSoap解析页面内容
# 创建日期：2018/1/24
# -------------------------------------------------------------------------

from bs4 import BeautifulSoup
from pegasus.crawlbot.chap01.common import download

def scrape(html):
    soup = BeautifulSoup(html)
    tr = soup.find(attrs={'id':'places_area__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    area = td.text

if __name__ == '__main__':
    html = download("http://example.webscraping.com/view/United-Kingdom-239'")
    print(scrape(html))