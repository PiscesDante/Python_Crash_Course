def upper_lower_func() :
    name = "ada lovelace"
    print(name.title()) # title()函数以首字母大写的形式显示每个单词
    print(name.upper()) # upper()函数将字符串中的每个字母都改成大写
    print(name.lower()) # lower()函数将字符串中的每个字母都改成小写

def convert_func() :
    msg = "iPhone X"
    fixed_msg = ""
    for letter in msg :
        if letter.isupper() :
            fixed_msg += letter.lower()
        else : 
            fixed_msg += letter.upper()
    print(fixed_msg)

def adhere_string() :
    first_name = "ada"
    last_name = "lovelace"
    full_name = first_name + " " + last_name # 字符串的拼接
    print(full_name)
    welcome_msg = "Hello, " + full_name.title() + "!"
    print(welcome_msg)

# ===========================================

adhere_string()