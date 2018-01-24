1. 网络爬虫的用处
不依赖API去访问所需的在线数据

2. 当抓取的数据是现实生活中的真实数据（如 营业地址、电话清单）时，是允许转载的。
但是，如果是原创数据，如意见和评论，通常就会受到版权限制，而不能转载。

要求下载请求的速度需要限定在一个合理值之内，并且还需要设定一个专属的用户代理来标识自己。

3. 在深入讨论爬取一个网站之前，我们首先需要对目标站点的规模和结构进行一定程度的了解。
网站的robots.txt和sitemap文件都可以为我们提供一定的帮助。
http://www.robotstxt.org
User-agent:*
Crawl-delay:5
Disallow:/trap

http://www.sitemaps.org/protocol.html
<urlset><url><loc>http://excample.webscraping.com/Af-1</loc></url></urlset>

4. 构建网站的技术类型 - builtwith模块。


