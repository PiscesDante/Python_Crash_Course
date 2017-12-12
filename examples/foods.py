my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods_copy = my_foods[:] # 复制一份
my_foods_copy.append('beef')
print(my_foods)
print(my_foods_copy)

my_foods_copy2 = my_foods # 这样是起了个别名，实际的列表对象来自一个地址
my_foods_copy2.append('mushroom')
print(my_foods)
print(my_foods_copy2)