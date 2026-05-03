class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class User:
    def __init__(self,name, is_premium=False):
       self.user_name = name
       self.is_premium = is_premium

class ShoppingCart:
    def __init__(self,user):
        self.user=user
        self.items=[]
    
    def add_product(self,product):
        self.items.append(product)
        print(f"Added {product.name} to {self.user.user_name}'s cart.")
   
    def remove_product(self,product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from cart.")
            else:
                print(f"Error: {product_name} not found in cart.")

    def calculate_total_cost(self):
        total= sum(item.price for item in self.items)
        if self.user.is_premium:
            discount = total*0.10
            total-=discount
            print(f"Premium Discount Applied: -Rs. {discount}")

        return total
    
    def generate_invoice(self):
        print(f"\n--- INVOICE FOR {self.user.user_name.upper()} ---")
        if not self.items:
            print("Your cart is empty.")
            return

        for item in self.items:
            print(f"- {item.name}: Rs. {item.price}")
        
        final_total = self.calculate_total_cost()
        print(f"TOTAL AMOUNT DUE: Rs. {final_total}")
        print("--------------------------\n")


if __name__ =="__main__":
    # Create some products
    p1 = Product("Laptop", 120000)
    p2 = Product("Mouse", 1500)
    p3 = Product("Keyboard", 4500)

    # Create a Premium User
    customer = User("Alice", is_premium=True)

    # Start shopping
    cart = ShoppingCart(customer)
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    # Remove an item
    cart.remove_product("Mouse")

    # Generate the final bill
    cart.generate_invoice()