motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改一个元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 追加一个元素
motorcycles.append('harry')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

# 插入一个元素
motorcycles.insert(0, 'jili')
print(motorcycles)

# 删除一个元素
del motorcycles[0]
print(motorcycles)

# 使用pop()方法来删除元素
print('=' * 50)
poped_moto = motorcycles.pop()
print(motorcycles)
print(poped_moto)