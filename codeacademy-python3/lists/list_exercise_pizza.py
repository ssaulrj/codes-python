toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print('We sell '+str(num_pizzas)+ ' different kinds of pizza!')

pizzas = list(zip(prices, toppings))
print('pizzas '+ str(pizzas))

pizzas.sort()
print('pizzas sort()' + str(pizzas))

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]

#Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizzas[0:3]
print('three_cheapest' + str(three_cheapest))

#Your boss wants you to do some research on $2 slices. 
num_two_dollar_slices = prices.count(2)
print('num_two_dollar_slices '+ str(num_two_dollar_slices))
