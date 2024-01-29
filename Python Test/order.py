# Database for customers, products and order
customers = {}
products = {}
orders = []

# Function for adding a customer to the database
def add_customer(name, contact_details):
    customer_id = len(customers) + 1
    customers[customer_id] = {'name': name, 'contact_details': contact_details, 'order_history': []}
    return customer_id


# Function for removing customer from the database
def remove_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        print(f"Customer with ID {customer_id} removed successfully.")
    else:
        f"Customer with ID {customer_id} not found."

# Function for displaying customer details
def display_customer_details(customer_id):
        if customer_id in customers:
            customer = customers[customer_id]
            print(f"Customer ID: {customer_id}")
            print(f"Name: {customer['name']}")
            print(f"Contact Details: {customer['contact_details']}")
            print("Order History:")
            for order in customer['order_history']:
                print(f"Order ID: {order['order_id']}, Total Cost: ${order['total_cost']}")
                print("Products:")
                for product in order['products']:
                    print(f"  {product['name']}, Quantity: {product['quantity']}")
        else:
            print(f"Customer with ID {customer_id} not found.")

# Function for adding a product to the database
def add_product(name,price,quantity_in_stock):
    product_id = len(products) + 1
    products[product_id] = {'name': name, 'price': price, 'quantity_in_stock': quantity_in_stock}
    return product_id

# Function for placing an order
def place_order(customer_id,product_id,quantity):
    if customer_id in customers and product_id in products:
        product = products[product_id]
        if product['quantity_in_stock'] >= quantity:
            total_cost = product['price'] * quantity
            order_id = len(orders) + 1

            # Update product quantity
            product['quantity_in_stock'] -= 1

            # Add product to customer's order history
            customers[customer_id]['order_history'].append({
            'order_id': order_id,
            'total_cost': total_cost,
            'products': [{'name': product['name'], 'quantity': quantity}]
                })
        
            # Add order to the global order list
            orders.append({
            'order_id': order_id,
            'customer_id': customer_id,
            'total_cost': total_cost,
            'products': [{'name': product['name'], 'quantity': quantity}]
                })
        
            print(f"Product added to order successfully. Order ID: {order_id}")
        else:
            print("Not enough stock available.")
    else:
        print("Invalid customer or product ID.")

# Function for calculating total cost
def calculate_total_order_cost(order_id):
        for order in orders:
            if order['order_id'] == order_id:
                return order['total_cost']
        return None

# The reporting system function
def display_report():
        total_sales = sum(order['total_cost'] for order in orders)
        print(f"Total Sales: ${total_sales}")

        # Find the most popular product
        if products:
            most_popular_product = max(products.values(), key=lambda x: x['quantity_in_stock'])
            print(f"Most Popular Product: {most_popular_product['name']}")
        
        # Display customer's order history
        print("\nCustomer Order History:")
        for customer_id, customer in customers.items():
            print(f"Customer ID: {customer_id}, Name: {customer['name']}")
            for order in customer['order_history']:
                print(f"  Order ID: {order['order_id']}, Total Cost: ${order['total_cost']}")
                print("    Products:")
                for product in order['products']:
                    print(f"      {product['name']}, Quantity: {product['quantity']}")





# Main program
while True:
    print("\nCustomer Order Management System")
    print("1. Add Customer")
    print("2. Remove Customer")
    print("3. Display Customer Details")
    print("4. Add Product")
    print("5. Place an Order")
    print("6. Calculate Total Order Cost")
    print("7. Display Business Report")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        contact_details = input("Enter customer contact details: ")
        add_customer(name, contact_details)
        print(f"Add customer {name} successfully")

    elif choice == '2':
        customer_id = int(input("Enter customer ID to remove: "))
        remove_customer(customer_id)

    elif choice == '3':
        customer_id = int(input("Enter customer ID to display details: "))
        display_customer_details(customer_id)

    elif choice == '4':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity_in_stock = int(input("Enter quantity in stock: "))
        add_product(name, price, quantity_in_stock)

    elif choice == '5':
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        place_order(customer_id, product_id, quantity)

    elif choice == '6':
        order_id = int(input("Enter order ID to calculate total cost: "))
        total_cost = calculate_total_order_cost(order_id)
        if total_cost:
            print(f"Total Cost for Order ID {order_id}: ${total_cost}")
        else:
            print(f"Order with ID {order_id} not found.")

    elif choice == '7':
        display_report()


    elif choice == '8':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")