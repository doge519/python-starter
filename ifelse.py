#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 注释
'''
aaaa
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

a, b, c = 1, 2.0, "john"

s = 'ilovehh'
print s[0:5]
print s * 2

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list + tinylist


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组


print a
print b
print c


import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# raw_input("Press the enter key to exit.\n\n")

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

total = 'aa'
sDot = 'sDot'
dDot = 'dDot'
tDot = '''tDot
aa'''
if True:
    print tDot
else:
    print "jj"