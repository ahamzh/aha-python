#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
print("中文cn")
print(ord('中'))
print('\u4e2d\u6587')
print(chr(20013))

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x)
print(x.decode('utf-8'))
print(x.decode('utf-8').encode('utf-8'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('zhangsan'))

# 格式化
# 在Python中，采用的格式化方式和C语言是一致的，用%实现
print('%2d-%02d' % (3, 1))

# format()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
