places = ['Shanghai', 'Tokyo', 'Souel', 'Nagasaki', 'Hiroshima'] # 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
print(places) # 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始 Python 列表。
print(sorted(places)) # 使用 sorted() 按字母顺序打印这个列表，同时不要修改它。
print(places) # 再次打印该列表，核实排列顺序未变。
print(sorted(places, reverse = True)) # 使用 sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(places) # 再次打印该列表，核实排列顺序未变。
places.reverse()
print(places) # 使用 reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(places) # 使用 reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.sort()
print(places) # 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort(reverse = True)
print(places) # 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。