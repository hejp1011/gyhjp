#实现两数相加的方法
def jia(z,y):
    a=z+y
    print(z,'+',y ,'=',a)
    return a
jia(jia(1,2),6)
#实现两数相减的方法
def jian(z,y):
    b=z-y
    print(z, '-', y, '=', b)
    return b
jian(jian(3,1),30)
#实现两数相乘的方法
def cheng(z,y):
    c=z*y
    print(z, '*', y, '=', c)
cheng(3,5)
#实现两数相除的方法
def chu(z,y):
    if (y != 0):
        d=z/y
        print(z, '/', y, '=', d)
    else:
        print('除数不能为零')

chu(60,0)

#有参数有返回值
def aa(m,n,k):
    return "{}欠{}{}钱".format(m,n,k)
print(aa('小明','我','很多很多很多'))