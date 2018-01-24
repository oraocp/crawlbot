# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示网络爬虫的相关工具的用法
# 创建日期：2017/11/23
# -------------------------------------------------------------------------

import builtwith
import whois

sites = ['http://example.webscraping.com',
         'http://www.163.com']

if __name__ == '__main__':
    for site in sites:
        print('Analysis site [%s]:' % site)
        # 检查网站构建的技术类型
        print(builtwith.parse(site))
        print('')
        # 寻找网站所有者
        print(whois.whois(site))
        print('')
