from functools import reduce
import functools
import time
import webNews
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def metric(fn):
    @functools.wraps(fn)
    def wraper(*args,**kw):
        start=time.time()
        result=fn(*args,**kw)
        print('%s executed in %s ms' % (fn.__name__, time.time()-start))
        return result
    return wraper
def log(text):
    def decor(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wraper
    return decor
@log("fileText")
def do():
    for i in range(10000000):
        j=i
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
if __name__ == '__main__':
    lisa=Student('lisa',90)
    bart=Student('bare',59)
    lisa.age=8
    print(lisa.age)
    print(lisa._Student__score)# 把类私有变量改造成了_ClassName__Variable