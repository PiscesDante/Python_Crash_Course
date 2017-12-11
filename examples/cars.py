cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # 使用sort()函数进行永久排序
print(cars)

cars.sort(reverse = True) # 从大到小排序（字典序）
print(cars)

cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars2)) # 只进行临时排序，不影响原来列表的内容，实质是返回一个新的list
print(cars2)

# 反转列表
cars2.reverse() # 反转操作还是会改变内容，这里实质其实是列表的成员函数
print(cars2)