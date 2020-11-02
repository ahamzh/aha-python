# 循环
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
nameList = ['张三', "李四", "王五"]
for name in nameList:
    print(name)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。¬¬
age = 1
while age < 100:
    print(age)
    if age == 66:
        break
    age = age + 1
