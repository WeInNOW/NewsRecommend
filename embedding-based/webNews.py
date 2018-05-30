# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
# 有url 就可以获得对应的fileNews
url = 'https://www.tagesspiegel.de/sport/nach-1-0-sieg-ueber-burkina-faso-nigeria-ist-afrika-meister-2013/7763284.html'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'UTF-8'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')

#遍历每一个class=ts-article-body的节点-获得新闻内容；
for news in soup.select('.ts-article-header'):
    h2 = news.select('p')
    #只选择长度大于0的结果
    if len(h2) > 0:
        title = h2[0].text
        print(title)



