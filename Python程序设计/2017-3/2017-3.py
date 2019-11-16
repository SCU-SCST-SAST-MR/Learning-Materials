def productRndNum():
    import random
    rnd=random.randint(100,200)
    numberLst=[random.randint(100,200) for i in range(rnd)]
    return numberLst

def getDigNumber(numberList, digLst):
    lst=numberList[:]
    def Include(num):
        for i in digLst:
            if str(i) in str(num):
                return True
        else:
            return False
    lst=list(filter(Include,lst))
    return lst

def printOut(num26Lst, n):
    count=0
    for i in num26Lst:
        print("{0:>5d}".format(i),end="")
        count+=1
        if count%n==0:
            print()
    else:
        if count%n!=0:
            print()

def func(num):
    lst=[]
    for i in range(2,num):
        if num%i==0:
            lst.append(i)
    return lst


def getDivisorNum(num26Lst):
    lst1=[]
    for i in num26Lst:
        lst1+=func(i)
    return lst1

def staticResult(lst):
    dec={}
    for i in lst:
        dec[i]=dec.get(i,0)+1
    return dec

def printMax5Out(resultStatic):
    a=sorted(resultStatic.items(),key=lambda e:e[1],reverse=True)
    for i in range(5):
        print(a[i][0])

def delMultiDivisor(resultLst):
    a=list(set(resultLst))
    resultLst[:]=a[:]

def printDivisorToFile(n, resultLst):
     f1=open(n,"w")
     count=0
     for i in resultLst:
        f1.write("{0:>5d}".format(i))
        count+=1
        if count%8==0:
            f1.write("\n")
     f1.close()



if __name__ == "__main__":
    # ----产生随机整数-------
    numberLst = productRndNum()

    # ----找出包含数字2或6的整数，其中digLst包含数字2和6-----
    digLst=[2,6]
    num26Lst = getDigNumber(numberLst, digLst)
    printOut(num26Lst, 8)
#
# -----找出所有整数的因子-----
    resultLst = getDivisorNum(num26Lst)
# -----统计每个因子出现的次数-----
    resultStatic = staticResult(resultLst)
    printMax5Out(resultStatic)
#
# # ----删除resultLst中重复因子的多余份数，只保留一份-----
    delMultiDivisor(resultLst)
#
    print("===出现次数最多的数字===")
    printDivisorToFile("D:\\python编程\\考试\\复习参考题3\\result.txt", resultLst)