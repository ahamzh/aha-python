# 生成器
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

aList = [x * x for x in range(10)]
print(aList)

aGenerator = (x * x for x in range(10))
print(aGenerator)
print(next(aGenerator))
print(next(aGenerator))
print(next(aGenerator))

# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
for x in aGenerator:
    print(x)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def func_yield_one(num):
    while num < 10:
        num = num + 1
        yield num


for value in func_yield_one(0):
    print(value)
