def add_ingredients(*ingredients) :
    print("You just ordered: ")
    for ingredient in ingredients :
        print("- %s" % ingredient)

# =================main==================

add_ingredients('Cheese', 'Pepper', 'Tomato')