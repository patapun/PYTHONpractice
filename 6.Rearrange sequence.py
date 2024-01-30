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

    def update_quantity(self, product_id, new_quantity):
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
            print("Product quantity updated successfully.")
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

                    # Update customer's order history
                    customer_name = self.get_customer_name_by_product(product_id)
                    if customer_name:
                        order_history = self.customer_profiles[customer_name].get('order_history', [])
                        order_history.append({'product_id': product_id, 'product_name': self.inventory[product_id]['name'], 'quantity': deletion_quantity})
                        self.customer_profiles[customer_name]['order_history'] = order_history

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
                for order in order_history:
                    product_name = order['product_name']
                    quantity = order['quantity']
                    price = self.inventory.get(order['product_id'], {}).get('price', 0)
                    order_total = quantity * price
                    total_payment += order_total
                    print(f"Product: {product_name}, Quantity: {quantity}, Price: ${price}, Order Total: ${order_total}")
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
    """
    Text-based interface for customers to interact with the e-commerce platform.

    Returns:
    None
    """
    print("Welcome to the Text-based E-Commerce Platform!")

    # Create an instance of the ECommercePlatform class
    ecommerce_platform = ECommercePlatform()

    while True:
        print("\nMenu:")
        print("1. Create Customer Profile")
        print("2. Check Product Availability")
        print("3. Check Product Quantity")
        print("4. Start to Place Order")
        print("5. Update Product Quantity")
        print("6. Delete Product Quantity")
        print("7. Check Total Payment")
        print("8. Check Order history")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            # Get customer details from the user
            customer_name = input("Enter Customer Name: ")
            customer_id = int(input("Enter Customer ID: "))

            # Add customer profile to the platform
            ecommerce_platform.add_customer_profile(customer_name, customer_id)
            print("Customer profile created successfully!")

        elif choice == '2':
            # Get product_id from the user and check product availability
            product_id = int(input("Enter Product ID to check availability: "))
            if ecommerce_platform.check_product_availability(product_id):
                print("Product is available.")
            else:
                print("Product is not available.")

        elif choice == '3':
            # Get product_id from the user and check current quantity
            product_id = int(input("Enter Product ID to check current quantity: "))
            current_quantity = ecommerce_platform.check_current_quantity(product_id)
            print(f"Current quantity of the product: {current_quantity}")

        elif choice == '4':
            # Ask the user to input customer name
            customer_name = input("Enter Customer Name: ")

            # Get the customer ID based on the input
            customer_id = ecommerce_platform.get_customer_id(customer_name)

            if customer_id == -1:
                print(f"Customer with name '{customer_name}' not found. Please reenter the registered name.")
                continue

            # Get product details from the user
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Initial Quantity: "))
            price = float(input("Enter Product Price: "))
            description = input("Enter Product Description: ")

            # Add product to the inventory
            ecommerce_platform.add_product(product_id, name, quantity, price, description, customer_name)
            print("Product added to inventory successfully!")

        elif choice == '5':
            # Get product_id and new_quantity from the user and update product quantity
            product_id = int(input("Enter Product ID to update quantity: "))
            new_quantity = int(input("Enter New Quantity: "))
            ecommerce_platform.update_quantity(product_id, new_quantity)
            print("Product quantity updated successfully!")

        elif choice == '6':
            # Get product_id from the user and delete product from inventory
            product_id = int(input("Enter Product ID to delete: "))
            ecommerce_platform.delete_product(product_id)

        elif choice == '7':
            # Get customer name or ID from the user and check total payment
            customer_input = input("Enter Customer Name or ID to check total payment: ")
            ecommerce_platform.check_total_payment(customer_input)

        elif choice == '8':
            # Get customer name or ID from the user and check order history
            customer_input = input("Enter Customer Name or ID to check order history: ")
            ecommerce_platform.check_order_history(customer_input)

        elif choice == '9':
            print("Exiting the Text-based E-Commerce Platform. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, 9")


# Run the text-based interface
if __name__ == "__main__":
    text_interface()
