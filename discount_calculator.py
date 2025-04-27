print("Enter the price of the 10 products, I will tell you the final price after 10% discount.")
items = []
items_price = []
discounted_items_price = []
for i in range(2):
    item = input(f"Enter the item {i+1}: ")
    items.append(item)
    item_price = float(input("Enter the price of the item: "))
    discounted_item_price = item_price*0.90
    items_price.append(item_price)
    discounted_items_price.append(discounted_item_price)
print("\nItem\t\tOrginal Price\tDiscounted Price")
for i in range(len(items)):
    print(f"{items[i]:<15} ${items_price[i]:<15} ${discounted_items_price[i]:.2f}")
