file_object = open('zen_of_python.txt')
content = file_object.read()
print(content)
file_object.close()
print("==============================")

file_object = open('zen_of_python.txt')
for line in file_object :
    print(line.strip())
file_object.close()
print("==============================")

file_object = open('zen_of_python.txt') # 读取完毕之后记得关闭文件
content_list = list(file_object)
for line in content_list :
    print(line)
file_object.close()