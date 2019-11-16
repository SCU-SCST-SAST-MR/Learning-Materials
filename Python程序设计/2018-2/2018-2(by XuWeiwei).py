#  学号:1827406004
#  姓名:徐卫伟
#  IP:192.168.156.170
#  上传时间:2018/12/19 20:00:47

import math
import re

def func1(m, n):
    if m<=1 or n<=1:
        return None
    else:
        if m<n:
            m,n=n,m
        for i in range(2,n+1):
            if m%i==0 and n%i==0:
                return False
        return True

def func2(lst):
    count=0
    for j in range(1,len(lst)):
        for i in range(j):
            if lst[i]>lst[j]:
                count+=1
    return count
    
def func3(mat1,mat2):
    lst=[[sum([mat1[i][j]*mat2[j][a] for j in range(len(mat2))]) for a in range(len(mat2[0]))] for i in range(len(mat1))]
    return lst
    
def func4(lst):
    a=len(lst)
    b=int(a**0.5)
    lst1=[]
    for i in range(b):
        a=[]
        for c in range(b):
            a.append(lst[c+b*i])
        lst1.append(a)
    return lst1

def func5(sentence):

    a=sentence.split()
    dic={}
    for i in a:
        dic[i] = dic.get(i, 0) + 1
    b=list(sorted(dic.items(),key=lambda e:(e[1],e[0]),reverse=True))

    if len(b)<3:
        c=[]
        for i in range(len(b)):
            c.append(b[i][0])
        return c
    else:
        c=[]
        c.append(b[0][0])
        c.append(b[1][0])
        c.append(b[2][0])
        return c




def func6(word1,word2):
    i=set(list(word1))
    j=set(list(word2))
    a=len(i&j)
    b=len(i.difference(j))
    c=len(j.difference(i))
    return (a,b,c)
        
def func7(string1):
    a=list(string1.upper())
    dic={}
    for i in a:
        dic[i]=dic.get(i,0)+1
    b=list(sorted(dic.items(),key=lambda e:e[1],reverse=True))
    c=[b[0][0],b[0][1]]

    return c

def func8(string1):
    import  re
    a=re.findall("\d+",string1)

    def len3_5(x):
        if len(x)<=5 and len(x)>=3:
            return True

        return False

    def aveDigits(x):
        a=[int(i) for i in list(str(x))]
        b=sum(a)/len(a)
        return b

    lst=list(map(int,filter(len3_5,a)))
    lst.sort(key=aveDigits,reverse=True)
    if len(lst)==0:
        return None
    return lst







