
def decor1(f):
    pass
    return f

@decor1
def fun1():
    a=1
    b=2
    if b > 5:
        raise TypeError()
    return a+b

def func(a, b, c):
    print('a={} b={} c={}'.format(a,b,c))
    fun1()
    print('finish func')
    return a + b + c

def main():
    try:
        func(1,2,3)
    except TypeError:
        print('Error!!!!')
        return
    print('Ok')

if __name__ == "__main__":
    main()
