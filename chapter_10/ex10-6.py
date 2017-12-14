val1, val2 = input("Enter a number: ").split(' ')
try :
    add_res = int(val1) + int(val2)
except ValueError :
    print("Error: Input is not a number.")
else :
    print("The sum is %d" % add_res)