# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
aList = ['张三', '李四', 1, 2, 3]
print(len(aList))
print(aList)
print(aList[0], aList[2], aList[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
aList.append("王五")
print(aList[len(aList) - 1])

# 也可以把元素插入到指定的位置，比如索引号为1的位置
aList.insert(0, '张牧之')
print(aList)

# 要删除list末尾的元素，用pop()方法
print(aList.pop())
print(aList)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print(aList.pop(0))
print(aList)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
aList[0] = 'kkk'
print(aList)

# list元素也可以是另一个list
aList[0] = ["0.1", 0.2, 0.3]
print(aList)
