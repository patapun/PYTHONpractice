class ECommercePlatform:
    def __init__(self):
        # Initialize dictionaries to store customer profiles and product information
        self.customer_profiles = {}
        self.inventory = {}

    def add_customer_profile(self, customer_name, customer_id):
        """
        Add a customer profile to the e-commerce platform.

        Parameters:
        - customer_name (str): Name of the customer.
        - customer_id (int): Unique identifier for the customer.

        Returns:
        None
        """
        self.customer_profiles[customer_name] = {'customer_id': customer_id, 'cart': {}, 'order_history': []}

    def create_product_category(self, product_id, name, description, quantity, price):
        """
        Create a product category and add it to the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - description (str): Description of the product.
        - quantity (int): Initial quantity in stock.
        - price (float): Price of the product.

        Returns:
        None
        """
        self.inventory[product_id] = {'name': name, 'description': description, 'quantity': quantity, 'price': price}
        print("Product category created successfully.")

    def check_product_availability(self, product_id):
        """
        Check if a product is available in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.

        Returns:
        bool: True if the product is available, False otherwise.
        """
        return product_id in self.inventory

    def check_current_quantity(self, product_id):
        """
        Check the current quantity of a product in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.

        Returns:
        int: Current quantity of the product.
        """
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return 0  # Product not found, quantity is 0

    def add_product(self, product_id, name, quantity, price, description, customer_name):
        """
        Add a product to the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Initial quantity in stock.
        - price (float): Price of the product.
        - description (str): Description of the product.
        - customer_name (str): Customer name.

        Returns:
        None
        """
        if customer_name in self.customer_profiles:
            self.inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price, 'description': description}
            print("Product added to inventory successfully.")

            # Update customer's order history
            order_history = self.customer_profiles[customer_name].get('order_history', [])
            order_history.append({'product_id': product_id, 'product_name': name, 'quantity': quantity})
            self.customer_profiles[customer_name]['order_history'] = order_history

        else:
            print("Customer not found. Please reenter the registered customer name or ID.")

    def start_to_order(self, customer_name, product_id, name, quantity, price, description):
        """
        Start the order process by adding a product to the customer's cart.

        Parameters:
        - customer_name (str): Customer name.
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Initial quantity in stock.
        - price (float): Price of the product.
        - description (str): Description of the product.

        Returns:
        None
        """
        if customer_name in self.customer_profiles:
            if product_id in self.inventory:
                # Check product availability and update inventory
                if self.inventory[product_id]['quantity'] >= quantity:
                    # Add the product to the customer's cart
                    self.customer_profiles[customer_name]['cart'][product_id] = {
                        'name': name,
                        'quantity': quantity,
                        'price': price,
                        'description': description
                    }
                    print("Product added to the cart successfully.")

                    # Update product quantity in inventory
                    self.inventory[product_id]['quantity'] -= quantity

                    # Update customer's order history
                    order_history = self.customer_profiles[customer_name].get('order_history', [])
                    order_history.append({'product_id': product_id, 'product_name': name, 'quantity': quantity})
                    self.customer_profiles[customer_name]['order_history'] = order_history
                else:
                    print("Insufficient quantity in the inventory.")
            else:
                print("Product ID not found in inventory.")
        else:
            print("Customer not found. Please reenter the registered customer name.")

    def update_product_quantity_in_inventory(self, product_id, new_quantity):
        """
        Update the quantity of a product in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - new_quantity (int): New quantity to set.

        Returns:
        None
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] = new_quantity
            print("Product quantity updated successfully in inventory.")
        else:
            print("Product not found in inventory.")

    def delete_product(self, product_id):
        """
        Delete a product from the inventory, allowing the customer to input the deletion quantity.
        If the deletion quantity is less than or equal to the current product quantity,
        calculate the net quantity and store it back in the dictionary.
        If the deletion quantity is more than the current quantity, display an appropriate message.

        Parameters:
        - product_id (int): Unique identifier for the product.

        Returns:
        None
        """
        if product_id in self.inventory:
            current_quantity = self.inventory[product_id]['quantity']
            if current_quantity == 0:
                del self.inventory[product_id]
                print("Product deleted from inventory.")
            else:
                deletion_quantity = int(input(f"Enter deletion quantity (current quantity: {current_quantity}): "))
                if deletion_quantity <= current_quantity:
                    net_quantity = current_quantity - deletion_quantity
                    self.inventory[product_id]['quantity'] = net_quantity
                    print(f"{deletion_quantity} items deleted. Net quantity: {net_quantity}")
                else:
                    print(f"Couldn't delete. The current product has only {current_quantity} items.")
        else:
            print("Product not found in inventory. Unable to delete.")

    def check_total_payment(self, customer_name):
        """
        Check the total payment for a customer's order by customer name.

        Parameters:
        - customer_name (str): Customer name.

        Returns:
        None
        """
        found_customer = False

        # Check if the input is a customer name
        if customer_name in self.customer_profiles:
            found_customer = True

        if found_customer:
            order_history = self.customer_profiles[customer_name].get('order_history', [])
            if order_history:
                print(f"\nTotal Payment for Customer Name {customer_name}:")
                total_payment = 0
                product_totals = {}  # To store the latest quantity * price for each product category

                for order in reversed(order_history):
                    product_id = order['product_id']
                    quantity = order['quantity']
                    price = self.inventory.get(product_id, {}).get('price', 0)

                    if product_id not in product_totals:
                        product_totals[product_id] = quantity * price
                        total_payment += quantity * price

                # Print individual product totals
                for product_id, product_total in product_totals.items():
                    product_name = self.inventory.get(product_id, {}).get('name', 'Unknown Product')
                    print(f"Product: {product_name}, Order Total: ${product_total}")

                print(f"Total Payment: ${total_payment}")
            else:
                print(f"\nNo order history found for Customer Name {customer_name}.")
        else:
            print(f"Customer with name '{customer_name}' not found. Please reenter the registered name.")


    def check_order_history(self, customer_name):
        """
        Check the order history of a customer by customer name.

        Parameters:
        - customer_name (str): Customer name.

        Returns:
        None
        """
        found_customer = False

        # Check if the input is a customer name
        if customer_name in self.customer_profiles:
            found_customer = True

        if found_customer:
            order_history = self.customer_profiles[customer_name].get('order_history', [])
            if order_history:
                print(f"\nOrder History for Customer Name {customer_name}:")
                for order in order_history:
                    print(f"Product: {order['product_name']}, Quantity: {order['quantity']}")
            else:
                print(f"\nNo order history found for Customer Name {customer_name}.")
        else:
            print(f"Customer with name '{customer_name}' not found. Please reenter the registered name.")


def text_interface():
    print("Welcome to the Text-based E-Commerce Platform!")

    # Create an instance of the ECommercePlatform class
    ecommerce_platform = ECommercePlatform()

    while True:
        print("\nMenu:")
        print("1. Create Customer Profile")
        print("2. Create Product Category")
        print("3. Check Product Availability")
        print("4. Check Current Quantity")
        print("5. Start to Order")
        print("6. Update Product Quantity in Inventory")  # Updated menu item
        print("7. Delete Product from Inventory")
        print("8. Check Total Payment")
        print("9. Check Order history")
        print("10. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == '1':
            customer_name = input("Enter Customer Name: ")
            customer_id = int(input("Enter Customer ID: "))
            ecommerce_platform.add_customer_profile(customer_name, customer_id)
            print("Customer profile created successfully!")

        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            description = input("Enter Product Description: ")
            quantity = int(input("Enter Initial Quantity: "))
            price = float(input("Enter Product Price: "))
            ecommerce_platform.create_product_category(product_id, name, description, quantity, price)

        elif choice == '3':
            product_id = int(input("Enter Product ID to check availability: "))
            if ecommerce_platform.check_product_availability(product_id):
                print("Product is available.")
            else:
                print("Product is not available.")

        elif choice == '4':
            product_id = int(input("Enter Product ID to check current quantity: "))
            current_quantity = ecommerce_platform.check_current_quantity(product_id)
            print(f"Current quantity of the product: {current_quantity}")

        elif choice == '5':
            customer_name = input("Enter Customer Name: ")
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Initial Quantity: "))
            price = float(input("Enter Product Price: "))
            description = input("Enter Product Description: ")
            ecommerce_platform.start_to_order(customer_name, product_id, name, quantity, price, description)

        elif choice == '6':
            product_id = int(input("Enter Product ID to update quantity: "))
            new_quantity = int(input("Enter New Quantity: "))
            ecommerce_platform.update_product_quantity_in_inventory(product_id, new_quantity)
            print("Product quantity updated successfully in inventory!")

        elif choice == '7':
            product_id = int(input("Enter Product ID to delete: "))
            ecommerce_platform.delete_product(product_id)

        elif choice == '8':
            customer_input = input("Enter Customer Name or ID to check total payment: ")
            ecommerce_platform.check_total_payment(customer_input)

        elif choice == '9':
            customer_input = input("Enter Customer Name or ID to check order history: ")
            ecommerce_platform.check_order_history(customer_input)

        elif choice == '10':
            print("Exiting the Text-based E-Commerce Platform. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")


# Run the text-based interface
if __name__ == "__main__":
    text_interface()
