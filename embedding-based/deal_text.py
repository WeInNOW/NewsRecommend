import json
import re
# 先只考虑文本内容，自编码文章表示
def getWordFromNews():
    pattern =r'^(\d+):::(.*?):::(\d+)$'
    newsDict=[]
    with open('../news/RandomItemSample.txt') as f:
        for eachline in f:
            news=eachline.split(":::")
            newsDict.append(json.loads(news[1]))
    with open('../news/newsTxt.txt','w',encoding='utf-8') as f:
        for dic in newsDict:
            string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", " ",dic.get('text'))
            f.write(string)
            f.write('\n')
# 计算文章向量- 先只使用词袋表示：
