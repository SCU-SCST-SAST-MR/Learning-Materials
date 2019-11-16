def getNum(string):
    import re
    lst=re.findall("\d+",string)
    lst=list(map(int,lst))
    return lst


def prime(num):
    if num<=2:
        return False
    for i in range(2,num+1):
        if num%i==0:
            if i!=num:
                return False
            else:
                return True



def includeThreeorSeven(num):
    if "3"in str(num) or "7" in str(num):
        return True
    return False

def zuobiao(lst):
    if len(lst)%2!=0:
        lst[:]=lst[:len(lst)-1]
    a=[]
    b=[]
    for i in lst:
        b.append(i)
        if len(b)==2:
            a.append(b)
            b=[]
    return a

def sumDistance(lst,A):
    A=list(A)
    distance=0
    for i in range(len(lst)):
        a=((lst[i][0]-A[0])**2+(lst[i][1]-A[1])**2)**0.5
        distance+=a
    return distance

def avgDistanc(distance):
    avg =distance/len(lst)
    return avg


def getA():
    import random
    a=random.uniform(0,100)
    b=random.uniform(0,100)
    A=(a,b)

    return A


def getALLwords(string):
    import re
    s=re.findall("[A-Za-z]+",string)
    return s

def getASCII(str):
    sum=0
    for i in list(str):
        sum+=ord(i)
    return sum


if __name__=="__main__":
    A = getA()
    print("({0:>10.2f},{1:>10.2f})".format(A[0], A[1]))

    string="Regular296expression913patterns465are280compiled102into510a122series48of563bytecodes16which366are262then773executed361by50a949matching556engine509written126in451C760For379advanced982use201it502may282be666necessary566to631pay199careful685attention915to814how577the455engine309will349execute178a341given171RE279and52write744the69RE5 78in190a361certain466way726in969order667to310produce943bytecode760that203runs590faster423Optimization723is787not458covered30in250this747document66because396it803requires530that601you928have208a152good609understanding194of31the772matching17engine599internals806"
    lst=list(filter(prime,getNum(string)))
    lst=list(filter(includeThreeorSeven,lst))
    count=0
    for i in lst:
        print("{0:>10d}".format(i),end="")
        count+=1
        if count%2==0:
            print()
    if len(lst)%2!=0:
        print()

    zuobiaolst=zuobiao(lst)




    print("距离之和为：{0:>10.2f}".format(sumDistance(zuobiaolst,A)))
    print("平均距离为：{0:>10.2f},素数构成的点的坐标个数：{1:>4d}".format(avgDistanc(sumDistance(zuobiaolst,A)),len(zuobiaolst)))

    s=getALLwords(string)
    lst1=[]
    count=0
    print("单词转化为整数：")
    for i in s:
        print("{0:<8d}".format(getASCII(i)),end="")
        count+=1
        if count%10==0:
            print()

