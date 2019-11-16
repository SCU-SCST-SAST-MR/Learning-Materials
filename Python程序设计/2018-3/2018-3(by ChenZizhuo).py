import math
import re

def func1(y, m, d):
    lst = [31,28,31,30,31,30,31,31,30,31,30,31]
    date = 0
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        lst[1] = 29
    if m > 12 or m < 1:
        return -1
    if d <= 0 or lst[m-1] < d:
        return -1
    for i in range(m-1):
        date += lst[i]
    return date + d
y=int(input())
m=int(input())
d=int(input())
print(func1(y,m,d))

# def func2(m, n):
#     if m < 0 or n < 0:
#         return None
#     t = (n-2*m)/2
#     j = m - t
#     if t < 0 or j < 0:
#         return None
#     if t%1 != 0 or j%1 != 0:
#         return None
#     return int(j),int(t)
#
# def func3(lst):
#     lst.sort()
#     if len(lst) == 0 or len(lst) == 1:
#         return None
#     if len(lst) == 2:
#         return True
#     d = lst[1] - lst[0]
#     for i in range(1,len(lst)):
#         if lst[i] - lst[i-1] != d:
#             return False
#     return True
#
# def func4(lst):
#     if len(lst) == 0:
#         return None
#     for i in lst:
#         if type(i) != type(1):
#             return None
#     lst.sort()
#     if len(lst)%2 == 0:
#         idx = int(len(lst)/2)
#         return int((lst[idx] + lst[idx-1])/2)
#     else:
#         idx = int((len(lst) - 1)/2)
#         return int(lst[idx])
#
# def func5(sentence):
#     sentence = str.lower(sentence)
#     lst = sentence.split()
#     if len(lst) < 3 or len(lst) > 11:
#         return None
#     dct = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
#     ret = ''
#     for i in lst:
#         ret += dct[i]
#     return ret
#
# def func6(a,b,c,d):
#     s = set()
#     for x in range(a,b+1):
#         for y in range(c,d+1):
#             s.add(x/y)
#     return len(s)
#
# def func7(s1, s2, n):
#     w = len(s1)%n
#     if w != 0:
#         s1 += ' '*(n-w)
#     ret = ''
#     for i in range(len(s1)):
#         ret += s1[i]
#         if (i+1)%n == 0:
#             ret += s2
#     return ret
#
# def func8(sentence):
#     while re.search('<[_a-zA-Z0-9]*>',sentence) != None:
#         tag = re.search('<([_a-zA-Z0-9]*)>',sentence).group(1)
#         rep = '[' + tag.upper() + '-' + str(len(tag)) + ']'
#         sentence = re.sub('<[_a-zA-Z0-9]*>',rep,sentence,count=1)
#     return sentence
