#练习
# 第一组数据   张三,李四,王五,赵六,钱七
g=["张三","李四","王五","赵六","钱七"]
print(type(g))
print(g)
# 第二组数据    姓名 张三  年龄 18 性别 女  科目 语文 成绩 80
h={"姓名":"张三","年龄":"18","性别":"女","科目":"语文","成绩":"80"}
print(type(h))
print(h)
# 第三组数据   A，2,3,4,5,6,7,8,9，J,Q,K
i=["A",2,3,4,5,6,7,8,9,"J","Q","K"]
print(type(i))
print(i)
# 第四组数据  10000
j=10000
print(type(j))
print(j)
# 第五组数据  学生
k="学生"
print(type(k))
print(k)


# 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
a=20
if(a>=10):
    print(a,"大于等于10")
    print(a,"元能买红双喜")
    print(a,"元能买大前门")
else:
    print(a,"小于10")
    print(a,"元不能买玉溪")


# 成人票 200 未成年票100 60岁以上的老人票 150 小明今年18岁，去买票应该买那种票？
b=18
if(b>=18):
    print("小明能买成人票")
elif(b>60):
    print("小明能买老人票")
elif(b>=12 and b<18):
    print("小明能买未成年票")
# 打印出100以内奇数
for i in range(100):
    if(i%2==1):
     print(i)


# 打印出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
            print(j,"*",i,"=",i*j,'\t',end="")
    print()

#打印出100以内的质数
for m in range(2,101):
    k=2
    for n in range(2,m):
        if(m%n==0):
            break
        k=k+1
    if(k==m):
        print(m)




























