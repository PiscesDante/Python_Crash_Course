pizza_list = ['pepperoni', 'florenza', 'napolezi']
friend_pizzas = pizza_list[:] # 创建副本
friend_pizzas.append('turing')

print("My favorite pizzas are:")
for pizza in pizza_list :
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas :
    print(pizza.title())