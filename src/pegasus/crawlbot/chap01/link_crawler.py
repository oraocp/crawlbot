# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：第一个网络爬虫，演示下载网页的相关技术
# 创建日期：2018/1/20
# -------------------------------------------------------------------------

import datetime
import re
import time
from queue import Queue

from pegasus.crawlbot.chap01.common import download, normalize, get_domain, get_links, same_domain


class Throttle:
    """
    在下载同一域名下网页时，增加等待的动作，以避免太频繁抓取会被网站屏蔽。
    """

    def __init__(self, delay):
        # 设置下载每个域时应等待时间
        self.delay = delay
        # 保存访问每个域的最新时间
        self.domains = {}

    def wait(self, url):
        # 根据URL解析域名
        domain = get_domain(url)
        # 获取域名的时间
        last_accessed = self.domains.get(domain, None)

        if self.delay > 0 and last_accessed is not None:
            # 计算两次访问同一域的时间差是否大于阀值，如大于阀值，则等待相应时间
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)


def crawl_link(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1,
               headers=None, user_agent='wswp', proxies=None, num_retries=2):
    """
    抓取指定网页以及网页上的所有链接
    
    :param seed_url: 种子网页URL
    :param link_regex: 链接正则表达式
    :param delay: 抓取的延时时间
    :param max_depth: 最大链接深度
    :param max_urls: 最大链接数
    :param headers: 头信息
    :param user_agent: 代理名称
    :param proxies: 代理信息
    :param num_retries:  最大重试次数
    """

    # 设置队列，将种子网页入列
    crawl_queue = list()
    crawl_queue.append(seed_url)
    # 网页URL的深度
    seen = {seed_url: 0}
    num_urls = 0
    throttle = Throttle(delay)
    # 检查robots文件是否允许
    # rp = get_robots(urljoin(seed_url, '/robots.txt'))
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        # 进行robots.txt文件检查，略过
        # if not rp.can_fetch(user_agent, url): continue
        throttle.wait(url)
        html = download(url, headers, proxies=proxies, num_retries=num_retries)
        links = []

        depth = seen[url]
        if depth != max_depth:
            # 如果未超过最大深度， 则继续抓取
            for link in get_links(html):
                # 过滤掉不符合配置要求的链接
                if link_regex:
                    if not re.match(link_regex, link):
                        continue
                links.append(link)

            for link in links:
                link = normalize(seed_url, link)
                # 检查链接是否已经抓取过了
                if link not in seen:
                    seen[link] = depth + 1
                    # 检查链接是否在同一域内
                    if same_domain(seed_url, link):
                        # 将链接加入到爬取队列中
                        crawl_queue.append(link)

            num_urls += 1
            if num_urls == max_urls:
                break


if __name__ == '__main__':
    # 按链接抓取示例网站
    crawl_link("http://example.webscraping.com/", )
