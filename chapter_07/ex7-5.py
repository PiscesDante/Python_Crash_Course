while True :
    age = int(input("Enter your age: "))
    if age < 3 :
        print("Your cost is $0.")
    elif age <= 12 :
        print("Your cost is $10.")
    else :
        print("Your cost is $15.")
    is_continue = input("Continue or not (y/n) ? > ")
    if is_continue == 'n' :
        break