class ProductApp:
    def __init__(self):
        self.products = []
        self.product_id = 1

    # Function to add a product
    def add_product(self, name, category, price):
        product = {
            'id': self.product_id,
            'name': name,
            'category': category,
            'price': price
        }
        self.products.append(product)
        self.product_id += 1
        print(f"Product '{name}' added successfully!")

    # Function to update a product by ID
    def update_product(self, product_id, name=None, category=None, price=None):
        for product in self.products:
            if product['id'] == product_id:
                if name:
                    product['name'] = name
                if category:
                    product['category'] = category
                if price:
                    product['price'] = price
                print(f"Product with ID {product_id} updated successfully!")
                return
        print(f"Product with ID {product_id} not found.")

    # Function to delete a product by ID
    def delete_product(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                self.products.remove(product)
                print(f"Product with ID {product_id} deleted successfully!")
                return
        print(f"Product with ID {product_id} not found.")

    # Function to get product by ID
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        print(f"Product with ID {product_id} not found.")
        return None

    # Function to get all products
    def get_all_products(self):
        if not self.products:
            print("No products found.")
        else:
            for product in self.products:
                print(product)

    # Function to get products by category
    def get_products_by_category(self, category):
        products_in_category = [product for product in self.products if product['category'] == category]
        if not products_in_category:
            print(f"No products found in category '{category}'.")
        else:
            for product in products_in_category:
                print(product)

    # Function to get products within a price range
    def get_products_between_prices(self, low_price, high_price):
        products_in_price_range = [product for product in self.products if low_price <= product['price'] <= high_price]
        if not products_in_price_range:
            print(f"No products found between prices {low_price} and {high_price}.")
        else:
            for product in products_in_price_range:
                print(product)


# Main program loop for user input
def main():
    app = ProductApp()

    while True:
        print("\nProduct App Menu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Get Product By ID")
        print("5. Get All Products")
        print("6. Get Products By Category")
        print("7. Get Products Between Prices")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            app.add_product(name, category, price)

        elif choice == 2:
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name (leave blank to skip): ")
            category = input("Enter new product category (leave blank to skip): ")
            price = input("Enter new product price (leave blank to skip): ")
            app.update_product(product_id, name or None, category or None, float(price) if price else None)

        elif choice == 3:
            product_id = int(input("Enter product ID to delete: "))
            app.delete_product(product_id)

        elif choice == 4:
            product_id = int(input("Enter product ID to retrieve: "))
            product = app.get_product_by_id(product_id)
            if product:
                print(product)

        elif choice == 5:
            app.get_all_products()

        elif choice == 6:
            category = input("Enter category: ")
            app.get_products_by_category(category)

        elif choice == 7:
            low_price = float(input("Enter minimum price: "))
            high_price = float(input("Enter maximum price: "))
            app.get_products_between_prices(low_price, high_price)

        elif choice == 8:
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
