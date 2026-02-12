#4 built-in data types in Python used to store collections of data 
#List = [] ordered, mutable, allows duplicate elements
#Tuple = () ordered, immutable, allows duplicate elements
#Set = {} unordered, mutable, no duplicate elements
#Dictionary = {key:value}

#define a dictionary (key/value) pairs
####
### https://youtu.be/ix9cRaBkVe0?si=6s1ubFwyGH1Qm2_J&t=9489
clear = "\n" * 100
print(clear)
print("Welcome to the Grocery Store")
print("------------------------")


foods =  [] #creates an empty list
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of {food}: "))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid price. Please enter a number.")

print("\n----- YOUR CART -----\n")

total=0
for food in foods:
    print(f"{food}")

for price in prices:
    total += price

print(f"Your total is: ${total:.2f}")

total=0
for i in range(len(foods)):
    print(f"{foods[i]} \t {prices[i]:.2f}")
    total = total + prices[i]
print(f"Your total is: ${total:.2f}")

