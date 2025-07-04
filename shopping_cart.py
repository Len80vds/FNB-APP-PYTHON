
#create_shopping_cart program that asks the user to add items to a shopping cart
#have an exit clause if the users stop adding items
#at the end show the total price of the items in the cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR SHOPPING CART-------") 

for food in foods:
    print(food,end=' ')

for price in prices:
    total += price

print("\n")
print(f"Your total is: R{total}")
