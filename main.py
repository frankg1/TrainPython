#-*- coding:utf-8 -*-
import ast

######## 1
lis=[2,2,2,3,2,222,2,2,2]
#枚举函数去处理list 不需要用到i了
for i ,item in enumerate(lis):
    print(i,item)
#枚举类型可以接受第二个参数
for i ,item in enumerate(lis,1):
    print(i,item)

######### 2 字典和集合 这个字典解析还是很有用的 可可以将这个list'成功的转化为字典
lis=['gx','zlb','dhb','zwl','zwl']

dic={i: lis[i] for i in range(4)}
print(dic)
#集合的生成  还可以自动去重
my_set={lis[i] for i in range(5)}
print(my_set)

#将集合再转化为list
lis=[i for i in my_set]
print(lis )

#########3 将字符串中的list提取出来
#这是古典做法
expr = "[1, 2, 3]"
my_list = eval(expr)
print(my_list)

#这是高级做法  安全性更高，因为上面的做法不会防止用户恶意的输入。
my_list = ast.literal_eval(expr)
print(my_list)

#json就是属于 python的字典类型  python 的字典类型更加强大
test="{\"name\":\"gx\"}"
test=ast.literal_eval(test)
print(test)
print(type(test))
print(test['name'])

#########4 直接输出lis的逆序
lis=['a','b','c','d']
print(lis[::-1])
lis.reverse()  #其实也是一样的效果
print(lis)

#########5 三元运算 很简单的选择题。
lis=[]
color='red' if len(lis)==0 else 'black'
print(color)