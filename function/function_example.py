# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。


def func_add(a, b):
    return a + b


print(func_add(1, 2))


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def func_blank():
    pass


print(func_blank())


# 参数检查
# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现


def func_add_1(a, b):
    if not isinstance(a, (int, float)):
        print("a参数类型不对")
        return
    if not isinstance(b, (int, float)):
        print("b参数类型不对")
        return
    return a + b


func_add_1("1", "2")


# 返回多个值
# 函数可以返回多个值吗？答案是肯定的。

def func_two_result(a, b):
    return a + b, a - b


print(func_two_result(1, 2))


# 函数的参数
# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3))


# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3, 4, 5, 6]))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。


def printSomeThing(name, age, **kwargs):
    print(name, age, kwargs)


printSomeThing("张三", 11, sex="男", info="未婚")


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# person("张三", 11, city="杭州", job="开发")

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person("张三", 11, "a", "b", "c", city="杭州", job="开发")


# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
