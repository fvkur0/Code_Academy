toppings = ("pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms")
prices = (2, 6, 1, 3, 2, 7, 2)

toppings_and_prices = zip(prices, toppings)
print(list(toppings_and_prices))

#zip creates a tuple
#a tuple is an immutable list

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print ("We sell", num_pizzas, "different kinds of pizza! ")

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"],
]
#print(pizza_and_prices)
pizza_and_prices = sorted(pizza_and_prices)
#print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop(-1)

pizza_and_prices.insert(-2, [2.5, "peppers"])
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)