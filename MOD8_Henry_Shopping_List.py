# Armando Gomez
# CSC500 - Module 8 Portfolio Project
# Henry the Pug's Bakery Shopping Cart 🐶🍞

"""
🐶 Henry the Pug is checking inventory for his bakery.
This py program will allow Mr. Henry to manage his ingredient inventory with this shopping cart.
Henry  will be able to add, modify, remove stock, and print his final list before checking out.
"""

# Step 1: Define the ItemToPurchase class
# This class stores the ingredients, (name, price, quantity, and description).
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description=""):
        """Initialize item with name, price, quantity, and description"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        """Display ingredient name, quantity, price, and total cost"""
        total_cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total_cost:.2f}")


# Step 2: Define the ShoppingCart class
# This class manages Henry's cart, storing ingredients and allowing changes.
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Start shopping cart with customer name and date"""
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Step 4: Implement add_item() method
    # Adds a new ingredient to Henrys shopping cart.
    def add_item(self, item):
        """Add an ingredient to Henry's cart"""
        self.cart_items.append(item)

    # Step 4: Implement remove_item() method
    # Removes an ingredient by given name.
    def remove_item(self, item_name):
        """Removes  ingredient"""
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                print(f"❌ Removed {item_name} from cart.")
                return
        print("⚠️ Item not found in this cart. Nothing removed.")

    # Step 4: Implement modify_item() method
    # Modifies an item's description, price, and/or quantity.
    def modify_item(self, modified_item):
        """Modify an item’s description, price, and/or quantity"""
        for item in self.cart_items:
            if item.name == modified_item.name:
                if modified_item.description:
                    item.description = modified_item.description
                if modified_item.price > 0:
                    item.price = modified_item.price
                if modified_item.quantity > 0:
                    item.quantity = modified_item.quantity
                print(f"🔄 Updated {item.name} details.")
                return
        print("⚠️ Item not found in cart. Nothing modified.")

    # Step 4: Implement get_num_items_in_cart() method
    # Returns the total number of ingredients in the cart.
    def get_num_items_in_cart(self):
        """Return total quantity of all items in cart"""
        return sum(item.quantity for item in self.cart_items)

    # Step 4: Implement get_cost_of_cart() method
    # Returns the total cost of all ingredients in the cart.
    def get_cost_of_cart(self):
        """Return total cost of items in cart"""
        return sum(item.price * item.quantity for item in self.cart_items)

    # Step 6: Implement print_total() method
    # Displays the full list of ingredients and total cost.
    def print_total(self):
        """Print Henry’s full shopping cart"""
        print(f"\n🛒 {self.customer_name}'s Bakery Shopping Cart - {self.current_date}")
        print(f"Total Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("🥺 SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\n💰 Total Cost: ${self.get_cost_of_cart():.2f}")

    # Step 6: Implement print_descriptions() method
    # Displays the descriptions of all ingredients in the cart.
    def print_descriptions(self):
        """Print descriptions of all items"""
        print(f"\n📜 {self.customer_name}'s Ingredient List - {self.current_date}")
        print("📝 Ingredients:")
        for item in self.cart_items:
            print(f"🔹 {item.name}: {item.description}")


# Step 5: Implement print_menu() function
# Provides an interactive menu for Henry to manage his shopping cart.
def print_menu(cart):
    """Display the menu and handle Henry’s choices"""
    while True:
        print("\n🍞 PUG BAKERY MENU")
        print("a - Add ingredient to cart")
        print("r - Remove ingredient from cart")
        print("c - Change ingredient quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit & Checkout")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':  # Step 8: Add Item
            name = input("Enter the ingredient name: ")
            description = input("Enter the ingredient description: ")
            price = float(input("Enter the ingredient price: "))
            quantity = int(input("Enter the ingredient quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)

        elif choice == 'r':  # Step 9: Remove Item
            name = input("Enter the name of the ingredient to remove: ")
            cart.remove_item(name)

        elif choice == 'c':  # Step 10: Modify Item
            name = input("Enter the name of the ingredient to modify: ")
            price = float(input("Enter the new price (or 0 to keep the same): "))
            quantity = int(input("Enter the new quantity (or 0 to keep the same): "))
            description = input("Enter the new description (or leave blank to keep the same): ")
            modified_item = ItemToPurchase(name, price, quantity, description)
            cart.modify_item(modified_item)

        elif choice == 'i':  # Step 6: Print Descriptions
            cart.print_descriptions()

        elif choice == 'o':  # Step 6: Print Shopping Cart
            cart.print_total()

        elif choice == 'q':  # Step 5: Quit
            print("\n🛍️ Checking out... Here’s your final receipt!")
            cart.print_total()
            print("🐶 Henry is ready to bake! 🥐👨‍🍳")
            break

        else:
            print("⚠️ Invalid option. Please try again.")


# Step 7: Launch user input for customer details, run this program
if __name__ == "__main__":
    # Prompt user for customer name and date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print(f"\n🐶 {customer_name}'s Bakery S- Mart Shopping - {current_date}")

    # Creates Henry's shopping cart
    henry_cart = ShoppingCart(customer_name, current_date)

    # Run the menu system for shopping cart
    print_menu(henry_cart)
