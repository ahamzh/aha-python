# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
aSet = set(["1", "1", "2", "3"])
print(aSet)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
aSet.add("2")
print(aSet)
# 通过remove(key)方法可以删除元素
aSet.remove("1")
print(aSet)
