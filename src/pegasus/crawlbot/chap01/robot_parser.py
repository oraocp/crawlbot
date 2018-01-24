# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：robots文件解析演示
# 创建日期：2018/1/18
# 说明：
# 大多数网站都会定义robots.txt文件，这样可以让爬虫了解该网站抓取时存在哪些限制。
# 虽然这些限制仅仅作为建议给出，但是良好的网络公民都应当遵守这些限制
# 关于robots.tx协议的更多信息可以参见http://www.robotstxt.org
# robots.txt中内容的示范：
#     User-agent:*         //表示搜索爬虫的名称 ，*表示对任何代理都有效
#     Disallow: test/*     //表示不允许抓取的条目
#     Allow:  publi        //表示允许抓取的条目
# -------------------------------------------------------------------------

from urllib.robotparser import RobotFileParser

"""
RootFileParser是urllib库中专门解析robots.txt文件的，使用方法简介如下：

1.set_url(url) 设置robotx.txt文件的链接。如果已经在创建RobotFileParser对象时传入了链接，那就不需要使用这个方法设置了。
2.read()       读取robots.txt文件并进行分析；一定要调用这个方法，否则接下来的判断都是False
3.parse()      用来解析robots.txt文件，传入参数是robots.txt某些行的内容
4.can_fetch()  方法传入2个参数：user-agent, url，如果可以抓取这个URL， 返回True； 否则返回False
5.mtime()      返回上次抓取和分析robots.txt的时间
6.modified()   将当前时间设置为上次抓取和分析robots.txt的时间
"""


def main():
    rb = RobotFileParser()
    rb.set_url("http://www.jianshu.com/robots.txt")
    # 也可以直接如下设置：
    # rb = RobotFileparser("http://www.jianshu.com/robots.txt")
    rb.read()
    print(rb.can_fetch('*', "http://www.jianshu.com/p/b67554025d7d"))
    # Disallow: search
    print(rb.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))


if __name__ == '__main__':
    main()
