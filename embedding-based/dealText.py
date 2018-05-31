import json
import re
import numpy as np
import tensorflow as tf
# LSTM-autoencoder
from LSTMAutoencoder import *

tf.reset_default_graph()


# W1 6000 * 500 b:500  -> h
batch_num = 128
input_num=6000
hidden_num = 500
step_num = 8
elem_num = 1
iteration = 1000 #迭代次数


def autoEncoder(inputArray):
    p_input = tf.placeholder(tf.float32, shape=(batch_num, step_num, elem_num))
    p_inputs = [tf.squeeze(t, [1]) for t in tf.split(p_input, step_num, 1)]
    cell = tf.nn.rnn_cell.LSTMCell(hidden_num, use_peepholes=True)
    ae = LSTMAutoencoder(hidden_num, p_inputs, cell=cell, decode_without_input=True)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for i in range(iteration):
            """Random sequences.
              Every sequence has size batch_num * step_num * elem_num 
              Each step number increases 1 by 1.
              An initial number of each sequence is in the range from 0 to 19.
              (ex. [8. 9. 10. 11. 12. 13. 14. 15])
            """
            r = np.array(inputArray)
            r = np.tile(r, (1, step_num, elem_num))
            d = np.linspace(0, step_num, step_num, endpoint=False).reshape([1, step_num, elem_num])
            d = np.tile(d, (batch_num, 1, 1))
            random_sequences = r + d

            (loss_val, _) = sess.run([ae.loss, ae.train], {p_input: random_sequences})
            print('iter %d:' % (i + 1), loss_val)

        (input_, output_) = sess.run([ae.input_, ae.output_], {p_input: r + d})
        print('train result :')
        print('input :', input_[0, :, :].flatten())
        print('output :', output_[0, :, :].flatten())

def autoEncode(inputArray):
    W1= np.random.random((input_num,hidden_num)) #初始值
    b1=np.random.random(hidden_num)
    W2= np.random.random((input_num,hidden_num)) #初始值
    b1=np.random.random(hidden_num)
    for i in range(iteration):
        hiddenVector=W1*inputArray + b1



# 先只考虑文本内容
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
    distinctWord=set() # 集合再转为list- 与下标有关的；
    wordFrequence=[]
    allArticleVector=[]
    with open('../news/newsTxt.txt',encoding='utf-8') as f:
        for eachline in f:
            if len(eachline) < 5:
                continue
            distinctWord=distinctWord.union(set(eachline.split()))
            wordFrequence.append(wordBag(eachline))
    #print(len(distinctWord)) # 5k 个特征词 共计17k个词
    wordList=list(distinctWord)
    for freqDict in wordFrequence:
        articleVector=[]
        for word in wordList:
            articleVector.append(freqDict.get(word,0)) # 已获得向量；
        print(articleVector)
        '''
        将6000维 压缩到 500 维 ~~ 词袋
        '''
        hiddenVector=autoEncode(articleVector)
        break
        allArticleVector.append(articleVector)


# 计算文章向量- 先只使用词袋表示：
def wordBag(strs):
    vector=dict() # 词与频率
    bags=strs.split()
    for word in bags:
        vector[word]=vector.get(word,0)+1
    return vector
if __name__ == '__main__':
    r=np.random.random(3)
    print(r)