# # [1,60,30,90,100,20,70.59,69,71,80,84]
# for i in [1,60,30,90,100,20,70,59,69,71,80,84]:
#     print(i)
#     if(i<60):
#         print(i,"为不及格")
#     if(i>60 and i<70):
#         print(i,"为及格")
#     if(i>70 and i<80):
#         print(i,"为良好")
# else:
#     print(i,"为优秀")

# #成绩0-59不及格，60-70及格 70-80 良好 80以上是优秀    [90,100,81,84]判断下改组成绩是否全部都是优秀
# a=0
# for j in [90,100,81,84]:
#     if(j<80):
#         a=1
# if(a==0):
#     print("为优秀")
# else:
#     print("垃圾")


# # "01010010001110001001001010101010010101" 计算下几个0 几个1
# b=0
# c=0
# a="01010010001110001001001010101010010101"
# for i in a:
#     if(i=="0"):
#         b=b+1
#     if(i=="1"):
#         c=c+1
# print(b,"个0",c,"个1")
#
# #求1+2+3+4...+100
# a=0
# i=1
# while(i<=100):
#     a= a+i
#     i=i+1
# print(a)

#
# #求出10的阶乘
# a=1
# i=10
# # while(i>=1):
# #     a=a*i
# #     i=i-1
# # print(a)
#
# # 字符串切片
# a="qwertyuiop"
# print(a[1:5])
# print(a[-5:-2])
#
# #
# #按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

def juge_3_2(a):
    # 第一步：统一符号  对字符串的处理，用replace（）
    # a=input()
    a=a.replace("''",'"')
    # 第二步：去掉中括号 字符串截取  [::]
    a=a[2:-2]
    # print(a)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b=a.split('" , "')
    # print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    d={}
    for i in b:
        c=i[1:]
    # 第五步：统计相同的数字个数  用字典去统计
        if c in d:
            d[c]=d[c]+1
        else:
            d[c]=1
    # print(d)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    m=1#key对应的数值有3的，如果没有则为m=0
    n=1#key对应的数值有3的，如果没有则为n=0
    for e in d:
        if(d[e]==3):
            m=1
        if(d[e]==2):
            n=1
    if(m==1 and n==1):
        print('这把三带二带飞')
    else:
        print('要王炸何用')
# for a in range(3):
#     juge_3_2()

with open ("D:\\softwareData\\python\\gyhjp\\demo\\day04\\lianxi_day04.txt",'r') as f:
    g=f.readlines()
    for h in g:
        h=h.replace('\n',"")
        print(h)
        juge_3_2(h)



# a='1,2,3,4,5,6,7,8,9,10'
# print(a[3])
# print(a[:2])
# print(a[::2])
# print(a[2:])
# print(a.replace('2','6'))











