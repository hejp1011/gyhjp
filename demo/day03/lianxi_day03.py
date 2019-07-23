# # a='https://guoyasoft.com/check/opt'
# # xieyiming=a.split('://')[0]
# # print(xieyiming)
# # a=a.split('://')[1]
# # print(a)
# # ip=a[:a.find('/')]
# # print(ip)
# # uri=a[a.find('/'):]
# # print(uri)
# #
# #
# # b='https://www.jianshu.com:8080/u/yZq3ZV'
# # xieyi=b.split('://')[0]
# # print(xieyi)
# # b=b.split('://')[1]
# # print(b)
# # yuming=b[:b.find('m:')+1]
# # print(yuming)
# # uri=b[b.find('/'):]
# # print(uri)
# # duankou=b[b.find('m:')+2:b.find('/')]
# # print(duankou)
#
# # 增
# #append新增单个值
# a=[1,'aaa',333]
# a.append(2)
# a.append('qwretr')
# print(a)
# # 用+合并两个列表，形成一个新列表，不改变原列表元素
# b=['fdhyr',7,8,9]
# print(a+b)
#
# # 删
# # 根据下标删除某个元素
# a.pop(0)
# print(a)
# # 默认删除列表的最后的一个元素
# a.pop()
# print(a)
# # # 清空一个列表
# # a=[]
# # print(a)
# # a.clear()
# # print(a)
#
# # 改
# # 根据下标修改某个元素的值
# a[0]='abc'
# print(a)
# # 等价
# a[0],a[1]=111,999
# print(a)
#
#
# # 查
# #根据下标查询某个元素
# print(a[0])
# print(a[1])
# #遍历（借助循环）
# for i in a:
#     print(i)
# #截取
# # 截取部分数据
# print(a[1:3])
# #倒序
# print(a[::-1])
#
# # 成员判断
# if(999 in a):
#     print('存在列表中')
# else:
#     print('不存在列表中')
# #获取长度
# print(len(a))

# 字典
# 字典的特性：
# 1、字典中的key是惟一的
# 2、key是不可改变的
    # 元组（1,2,3）可以作为key，但（1，[3]）不可以作为key
# 字典中新增一对数据
a={}
a["姓名"]='哈哈'
print(a)
a[1]=666
print(a)
a[(1,2)]=666
print(a)

# 删
# 删除某一对值，pop参数只能为key
a.pop("姓名")
# del a["姓名"]
print(a)
# 清空字典
# a.clear()
# print(a)
# 改
a["姓名"]='嘻嘻'
print(a)

# 查
# 根据key查看value
print(a["姓名"])
# 遍历字典（借助循环）
for i in a:
    print(a[i])

#  字典合并
c={'姓名':'卡卡'}
d={'姓别':'未知'}
# c.update(d)
# print(c)
#两个字典合并，生成一个新的字典,不改变原来字典数据
print(dict(c,**d))
print(c)
print(d)

# 成员判断，只支持key
if ('姓名' in c):
    print('存在字典中')
else:
    print('不存在字典中')