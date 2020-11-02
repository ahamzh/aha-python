#!/usr/bin/python3

# 第一个注释
print("hello，word")  # 第二个注释

'''
多行注释
多行注释
'''
print('hello，python')

'''
多行语句
'''
sum = 1 + 2 \
      + 3
print(sum)

'''
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''
print(type(1000))
print(type(True))
print(type(1.23))
print(type(1 + 2j))

'''
字符串(String)
python中单引号和双引号使用完全相同。
使用三引号(\'''或""")可以指定一个多行字符串。
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''
str = '123456'
print(str[1:3])

'''
等待用户输入
'''
print(input("\n\n按下 enter 键后退出。\n"))

'''
Print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
'''
print('张三', end="")
print('李四', end="")


'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

