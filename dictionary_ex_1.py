def main():
    product_prices = {}
   
    # phase 1: To enter all the priodcur details and their prices.
    while True:
        product = input("Enter the name of the product (or 'done' to finish): ").strip()
        if product.lower() == "done":
            break
        try:
            price = float(input(f"Enter the price for '{product}': ").strip())
            product_prices[product] = price
           
        except ValueError:
            print("Please enter the correct value.")
           
   
    #phase 2: Looking up prices
    while True:
        query = input("Enter the name of the product to look up (or enter exit to stop): ").strip()
        if query.lower() == "exit":
            break
        if query in product_prices:
            print(f"The price of '{query}' is ${product_prices[query]:.2f}")
        else:
            print("Prodcut not found.")
           
if __name__ == "__main__":
    main()
           