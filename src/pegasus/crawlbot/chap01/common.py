# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：下载库通用模块，提供下载功能
# 创建日期：2018/1/21
# -------------------------------------------------------------------------

import re
from urllib.parse import urlparse, urldefrag, urljoin
from urllib.robotparser import RobotFileParser

import requests


def get_robots(url):
    """
    获取Robots解析器
    :param url: robots.txt存在路径
    :return: Robots解析器
    """
    rp = RobotFileParser()
    rp.set_url(url)
    rp.read()
    return rp


def download(url, headers=None, proxies=None, num_retries=2):
    """
    通过HTTP协议下载网页
    :param url: 网页URL地址
    :param headers: 头信息
    :param proxy:代理信息
    :param num_retries: 重试次数，默认为2次
    :return:
    """
    print("Downloading:", url)
    try:
        html = requests.get(url, headers=headers, proxies=proxies).text
    except Exception as e:
        print("Download error:", e)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


def get_links(html):
    """
    解析HTML文件中的链接地址，并返回所有匹配的结果
    :param html: 要分析的HTML文件
    :return: 匹配的结果
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


def get_domain(url):
    """
    获取URL中包括的域名
    :param url:
    :return:
    """
    o = urlparse(url)
    print(o)
    # 去除端口号
    idx = o.netloc.find(':')
    if idx != -1:
        return o.netloc[:idx]
    else:
        return o.netloc


def normalize(seed_url, link):
    #如果url包含一个片段标识符，则返回一个没有片段标识符的修改过的url
    link, _ = urldefrag(link)
    return urljoin(seed_url, link)


def same_domain(url1, url2):
    """
    判断两个URL的域名是否相等
    :param url1: URL1
    :param url2: URL2
    :return: 如果域名相等，返回True;否则返回False
    """
    return urlparse(url1).netloc == urlparse(url2).netloc


if __name__ == '__main__':
    print(get_domain('http://www.sina.com.cn/Eguido/Python.do'))
    print(get_domain('http://www.cwi.nl:8080/Eguido/Python.do'))
    # 对于IP地址的URL，返回IP地址
    print(get_domain('http://127.0.0.1:8080/Eguido/Python.do'))

    html = download("http://www.jianshu.com")
    for link in get_links(html):
        print(link)

    print(normalize("http://www.jianshu.com", "/qime/tm.ca"))

    rb = get_robots("http://www.jianshu.com/robots.txt")
    # Disallow: search
    print(rb.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
