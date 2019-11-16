#  学号:1927405024
#  姓名:哈昕依
#  IP:192.168.157.84
#  上传时间:2019/11/6 19:59:49

def func1(n):
      return n>=60


def func2(n):
    n1=n//50
    n2=(n%50)//30
    n3=(n-n1*50-n2*30)//10
    return n1*8+n2*4+n3


def func3(n):
    lst=[]
    for i in range(1,n):
        if i%2==0:
            lst.append(i**2)
    return sum(lst)

def func4(k):
    n=0
    for i in range(0,k):
        for j in range(0,k):
            if i+2*j<k:
                n+=1

    return n


def func5(a, b):
    if a%b==0 or b%a==0:
        return True
    else:
        return False

def func6(x):
    n=0
    lst=list(bin(x))
    lst.remove('b')
    for i in lst:
        if int(i)==1:
            n+=1

    return n

def func7(lst):
    if len(lst)<3:
        return None
    else:
        lst.sort()
        lst=lst[1:-1]
        a=int(sum(lst)//len(lst))
        return a
def isPrime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def func8(lst):
    alist=[]
    for i in lst:
        a=i%100
        b=(i-i%100)//100
        if isPrime(a) and isPrime(b):
            alist.append(i)
    return alist

if __name__ == '__main__':
    print(func1(17))
    print(func2(129))
    print(func3(17))
    print(func5(4,15))
    print(func4(56))
    print(func7([1,2,78]))
    print(func6(3567))
    print(func8([2,834,203,9797]))

