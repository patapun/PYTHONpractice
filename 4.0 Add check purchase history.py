class ECommercePlatform:
    def __init__(self):
        # Initialize dictionaries to store customer profiles and product information
        self.customer_profiles = {}
        self.inventory = {}

    def add_customer_profile(self, customer_id, customer_name):
        """
        Add a customer profile to the e-commerce platform.

        Parameters:
        - customer_id (int): Unique identifier for the customer.
        - customer_name (str): Name of the customer.

        Returns:
        None
        """
        self.customer_profiles[customer_id] = {'customer_name': customer_name, 'cart': {}}

    def add_product_name(self, product_id, name):
        """
        Add or update the name of a product in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.

        Returns:
        None
        """
        if product_id in self.inventory:
            self.inventory[product_id]['name'] = name
            print("Product name updated successfully.")
        else:
            print("Product not found in inventory. Please add the product first.")

    def add_product_quantity(self, product_id, quantity):
        """
        Add or update the quantity of a product in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - quantity (int): Quantity of the product.

        Returns:
        None
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] = quantity
            print("Product quantity updated successfully.")
        else:
            print("Product not found in inventory. Please add the product first.")

    def add_product_price(self, product_id, price):
        """
        Add or update the price of a product in the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - price (float): Price of the product.

        Returns:
        None
        """
        if product_id in self.inventory:
            self.inventory[product_id]['price'] = price
            print("Product price updated successfully.")
        else:
            print("Product not found in inventory. Please add the product first.")

    def add_product(self, product_id, name, quantity, price, description, customer_id):
        """
        Add a product to the inventory.

        Parameters:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product.
        - quantity (int): Initial quantity in stock.
        - price (float): Price of the product.
        - description (str): Description of the product.
        - customer_id (int): Customer ID.

        Returns:
        None
        """
        if customer_id in self.customer_profiles:
            self.inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price, 'description': description}
            print("Product added to inventory successfully.")
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
                else:
                    print(f"Couldn't delete. The current product has only {current_quantity} items.")
        else:
            print("Product not found in inventory. Unable to delete.")

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

    def get_customer_id(self, customer_input):
        """
        Get the customer ID based on the input (either customer name or ID).

        Parameters:
        - customer_input (str or int): Customer name or ID.

        Returns:
        int: Customer ID if found, -1 otherwise.
        """
        if isinstance(customer_input, int):
            return customer_input
        else:
            for cid, profile in self.customer_profiles.items():
                if profile['customer_name'] == customer_input:
                    return cid
            return -1

    def check_order_history(self, customer_input):
        """
        Check the order history of a customer by customer name or ID.

        Parameters:
        - customer_input (str or int): Customer name or ID.

        Returns:
        None
        """
        found_customer = False

        # Check if the input is a customer ID
        if isinstance(customer_input, int):
            if customer_input in self.customer_profiles:
                found_customer = True
                customer_id = customer_input
        else:
            # Check if the input is a customer name
            for cid, profile in self.customer_profiles.items():
                if profile['customer_name'] == customer_input:
                    found_customer = True
                    customer_id = cid
                    break

        if found_customer:
            order_history = self.customer_profiles[customer_id].get('order_history', [])
            if order_history:
                print(f"\nOrder History for Customer ID {customer_id} ({customer_input}):")
                for order in order_history:
                    print(f"Product: {order['product_name']}, Quantity: {order['quantity']}, Total Payment: ${order['total_payment']}")
            else:
                print(f"\nNo order history found for Customer ID {customer_id} ({customer_input}).")
        else:
            print(f"Customer with name or ID '{customer_input}' not found. Please reenter the registered name or ID.")


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
        print("2. Add Product to Inventory")
        print("3. Update Product Quantity")
        print("4. Delete Product from Inventory")
        print("5. Check Product Availability")
        print("6. Check Current Quantity")
        print("7. Check Order history")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            # Get customer details from the user
            customer_id = int(input("Enter Customer ID: "))
            customer_name = input("Enter Customer Name: ")

            # Add customer profile to the platform
            ecommerce_platform.add_customer_profile(customer_id, customer_name)
            print("Customer profile created successfully!")

        elif choice == '2':
            # Ask the user to input customer name or ID
            customer_input = input("Enter Customer Name or ID: ")

            # Get the customer ID based on the input
            customer_id = ecommerce_platform.get_customer_id(customer_input)

            if customer_id == -1:
                print(f"Customer with name or ID '{customer_input}' not found. Please reenter the registered name or ID.")
                continue

            # Get product details from the user
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Initial Quantity: "))
            price = float(input("Enter Product Price: "))
            description = input("Enter Product Description: ")

            # Add product to the inventory
            ecommerce_platform.add_product(product_id, name, quantity, price, description, customer_id)
            print("Product added to inventory successfully!")

        elif choice == '3':
            # Get product_id and new_quantity from the user and update product quantity
            product_id = int(input("Enter Product ID to update quantity: "))
            new_quantity = int(input("Enter New Quantity: "))
            ecommerce_platform.update_quantity(product_id, new_quantity)
            print("Product quantity updated successfully!")

        elif choice == '4':
            # Get product_id from the user and delete product from inventory
            product_id = int(input("Enter Product ID to delete: "))
            ecommerce_platform.delete_product(product_id)

        elif choice == '5':
            # Get product_id from the user and check product availability
            product_id = int(input("Enter Product ID to check availability: "))
            if ecommerce_platform.check_product_availability(product_id):
                print("Product is available.")
            else:
                print("Product is not available.")

        elif choice == '6':
            # Get product_id from the user and check current quantity
            product_id = int(input("Enter Product ID to check current quantity: "))
            current_quantity = ecommerce_platform.check_current_quantity(product_id)
            print(f"Current quantity of the product: {current_quantity}")

        elif choice == '7':
            print("Exiting the Text-based E-Commerce Platform. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7")


# Run the text-based interface
if __name__ == "__main__":
    text_interface()