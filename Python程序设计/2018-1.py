def func1(x):
    if x >= 0:
        y = 5*x
        return y
    else:
        y = 3 * (-1*x) + 1
        return y

def func2(x):
    if x >= 10:
        return 10
    elif x >= 8:
        return 8 * x**3
    elif x >= 3:
        return 3 * x**2
    elif x >= 0:
        return x + 1
    else:
        return -1 * x

def func3(m,n):
    if m < 0 or n < 0:
        return None
    lst = [x for x in range(m,n+1) if x % 2 == 1]
    return sum(lst)

def func4(m,n):
    def func(x):
        lst = []
        while x:
            lst.append(x % 10)
            x //= 10
        num = lst.count(2)
        return num
    lst_ = [func(x) for x in range(m,n+1)  if x>=0]
    return sum(lst_)

def func5(x):

    lst = []
    while x:
        lst.append(x % 10)
        x //= 10
    lst_ = []
    lst_.append(len(lst))
    lst_.append(sum(lst))
    lst_.append(max(lst))
    return lst_

def func6(m,n):
    if m <= 0 or n <= 0:
        return None
    elif m < 100:
        return m
    lst = []
    while m:
        lst.append(m % 10)
        m //= 10
    lst.reverse()
    lst[0] += n
    if lst[0] >= 10:
        lst[0] %= 10
    a = 0
    num = 0
    for x in lst:
        n = len(lst) - 1 - num
        num += 1
        a += x * 10**n
    return a

def func7(lst,k):
    lst[0:k]=lst[k - 1::-1]
    return lst

def func8(lst,v):

    def func(x):
        lst = []
        while x:
            lst.append(x % 10)
            x //= 10
        return sum(lst) / len(lst)

    lst1 = [x for x in lst if func(x) >= v]
    lst1.sort(reverse = True)
    return lst1



