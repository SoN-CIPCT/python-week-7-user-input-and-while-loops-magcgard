pizza_orders= ["pepperoni", "veggie", "meat lovah", "cheese"]
finished_pizzas= []
for pizza in pizza_orders[:]:
    print("Your pizza pie is finished!")
    pizza_orders.remove(pizza)
    finished_pizzas.append(pizza)
    print(f"The pizza {pizza} was made.")