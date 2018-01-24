# -------------------------------------------------------------------------
# 文件目的：网站地图解析演示
# 创建日期：2018/1/18
# 说明：
# 网站提供的Sitemap文件（即网站地图）可以帮助爬虫定位网站最新的内容，而无须爬取每一个网页
# 参见http://www.sitemaps.org/protocol.html获取网站地图标准的定义
# Sitemap分为三种格式：txt文本格式、xml格式、Sitemap索引格式
# 以百度Sitemap为例：<urlset><url><loc><lastmod><changefreq><priority>
# -------------------------------------------------------------------------

import json
import re
import xml.etree.ElementTree as ET


# 解析XML时，节点名称为Namespace+tag_name
def get_namespace(element):
    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''


def parse_sitemap(name, xmlfile):
    sitemap = SiteMap(name)
    tree = ET.parse(xmlfile)
    # 取得XML根节点，urlset
    root = tree.getroot()
    # 获得Namespace
    nm = get_namespace(root)
    for url in root.iter(nm + "url"):
        for child in url:
            loc = None
            lastmod = None
            changefreq = None
            priority = 0
            if child.tag == (nm + 'loc'):
                loc = child.text
            elif child.tag == (nm + 'lastmod'):
                lastmod = child.text
            elif child.tag == (nm + 'changefreq'):
                changefreq = child.text
            elif child.tag == (nm + 'priority'):
                priority = int(child.text)
            sitemap.urls.append(SiteUrl(loc, lastmod, changefreq, priority))
    return sitemap


class SiteMap(object):
    def __init__(self, name):
        self.name = name
        self.urls = []

    def __str__(self):
        return self.name


class SiteUrl(object):
    """
    URL属性
    """

    def __init__(self, loc, lastmod=None, changefreq=None, priority=0):
        self.loc = loc
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.priority = priority

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    sitemap = parse_sitemap("example", "sitemap.xml")
    print(sitemap)
    for url in sitemap.urls:
        print(url)
