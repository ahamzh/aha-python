# dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

aDict = {"张三": 1, "李四": 2, "王五": 3}
print(aDict)
print(aDict.get("张三"))
print("张三" in aDict)
print("kkk" in aDict)

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(aDict.pop("张三"))
print(aDict.pop("张三"))
print(aDict)
