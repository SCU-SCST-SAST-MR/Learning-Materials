def func1(r):
    import re
    numlist=re.findall(r"\d+",r)
    if len(numlist)%2!=0:
        numlist=numlist[0:len(numlist)-1]
    lst=[]
    for i in range(0,len(numlist)-1,2):
        lst.append(numlist[i]+numlist[i+1])
    lst=list(map(int,lst))

    return lst


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else: return True

def func2(lst):
    return list(set(lst))


def func3(num):
    sum=int(str(num)[len(str(num))-1])+int(str(num)[len(str(num))-2])
    return sum

def Sort(lst):
    lst.sort(key=func3)
    return lst


if __name__=="__main__":
    d="24 53 91   70 70 1   12 87 102 46 70 1   33 7 9 13 70 1 5 3 11 2 70 1  5 67 453 54 78 32 58 561 902 32 34 21 1045 143 17 13 271 79 13 9 13"
    numlist=func1(d)
    print(numlist)
    numlist=list(filter(prime,func2(numlist)))
    print(numlist)
    numlist=Sort(numlist)
    count=0
    for i in numlist:
        print("{0:>10d}".format(i),end="")
        count+=1
        if count%2==0:
            print()
    else:
        if count%2!=0:
            print()
    max1=max(numlist)
    min1=min(numlist)
    aver=sum(numlist)/len(numlist)
    print("最大值：{0:<10d}".format(max1))
    print("最小值：{0:<10d}".format(min1))
    print("平均值：{0:<10.3f}".format(aver))

