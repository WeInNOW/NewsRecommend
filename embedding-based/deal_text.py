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
def getVector():
    distinctWord=set()
    with open('../news/newsTxt.txt') as f:
        for eachline in f:
            if len(eachline) < 5:
                continue
            distinctWord=distinctWord.union(set(eachline.split()))
            wordBag(eachline)
    print(len(distinctWord))

# 计算文章向量- 先只使用词袋表示：
def wordBag(strs):
    words=[]  # 存的词，
    vector=[] # 向量
    bags=strs.split()
    for word in bags:
        if word not in words:

            words.append(word)
            vector.append(1)
        else:
            vector[words.index(word)] += 1
    return vector
if __name__ == '__main__':
    getVector()