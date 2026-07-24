print("-" * 35)

snack_name = "Chocolate"
snack_price = 30
snack_quantity = 5
snack_availability = True

print(f"Snack name: {snack_name}\nData Type: {type(snack_name)}\n\nSnack Price: {snack_price}\nData Type: {type(snack_price)}\n\nSnack Quantity: {snack_quantity}\nData Type: {type(snack_quantity)}\n\nSnack Availability: {snack_availability}\nData Type: {type(snack_availability)}\n")

total_price = snack_quantity * snack_price
print(f"Total Cost: {total_price}")

discounted_price = total_price - 10
print(f"Discounted Price: {discounted_price}")

restock = snack_quantity * 4
print(f"Restock: {restock}\n")

print(f"Is price less than K40? {snack_price < 40}\nIs there more than 10 stocks? {snack_quantity > 10}\nIs price exactly K30? {snack_price == 30}\n")

shop_name = "Lucky Sweets"
print(f"Shop Name: {shop_name}\nLetters present in snack name: {len(snack_name)}\nFirst letter of snack name: {snack_name[0]}\n")

price_1 = 300
price_2 = 500

print(f"Prices Before Swapping: Price 1: {price_1}, Price 2: {price_2}")

temporary_price = price_1
price_1 = price_2
price_2 = temporary_price

print(f"After Swapping Prices: Price 1: {price_1}, Price 2: {price_2}")
print("-" * 35)