import re
def readWordsFromFile(n):
    f1=open(n,"r")
    s1=f1.read()
    pattern=re.compile(r"[A-Za-z]+")
    wordlist=pattern.findall(s1)
    f1.close()
    return wordlist


def findMultiAlphaWords(wordlist,num):
    wordResultLst=[]
    newwordlist=wordlist[:]
    for i in newwordlist:
        k=i
        a=list(k.lower())
        for j in a:
            if a.count(j)>=num:
                wordResultLst.append(i)
                break
    return wordResultLst

def delMultiData(lst):
    a=list(set(lst))
    lst[:]=a[:]

def printWordLst(lst,num):
    count=0
    for i in lst:
        print("{0:20s}".format(i),end=" ")
        count+=1
        if count%num==0:
            print()
    print()


def getNumberOfWords(wordResultLst):
    numLst=[]
    for i in wordResultLst:
        a=list(i)
        b=list(map(ord,a))
        numLst.append(sum(b))
    return numLst

def sortByDigitalSum(numLst):
    def sumdigit(i):
        a=sum(map(int,list(str(i))))
        return a
    numLst.sort(key=sumdigit,reverse=True)
    return numLst

def printNumLst(numlst, num):
    count=0
    for i in numlst:
        print("{0:8d}".format(i),end=" ")
        count+=1
        if count%num==0:
            print()
    print()

def staticDigitalTimes(numlst):
    resultDic={}
    for i in numlst:
        a=list(str(i))
        a=list(map(int,a))
        for j in a:
            resultDic[j]=resultDic.get(j,0)+1
    return resultDic

def printDicToFile(n, dic):
    f1=open(n,"a")
    a=list(sorted(dic.items(),key=lambda e:e[1],reverse=True))
    f1.write("{0:<2d}".format(a[0][0])+":"+"{0:>3}".format(a[0][1]))
    f1.close()
    print("{0:<2d}".format(a[0][0])+":"+"{0:>3}".format(a[0][1]))


if __name__ == "__main__":
    # ----从data.txt文件中读取所有单词-------
    wordlst = readWordsFromFile(r"d:\python编程\考试\复习参考题2\data.txt")
    print("文件中单词个数:", len(wordlst))  # 输出单词个数
    # ----找出单词中，存在某个字母重复num次的单词-----
    wordResultLst = findMultiAlphaWords(wordlst, 2)
    print("至少含有重复2次的字母的单词：", len(wordResultLst))



    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    delMultiData(wordResultLst)
    print("===删除重复单词的多余单词后的结果===")
    printWordLst(wordResultLst, 4)  # 输出所有单词，每行输出4个单词

    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)

    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)  # 输出整数列表，每行输出5个整数

    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    print(resultDic)
    print("===出现次数最多的数字===")
    printDicToFile(r"d:\python编程\考试\复习参考题2\result.txt", resultDic)