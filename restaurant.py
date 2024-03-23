class Order():
    def __init__(self) -> None:
        self.items = []
        self.__subtotal = None
        self.__total = None
        self.__discount = 0

    def __calculate_price(self):
        self.__subtotal = sum([item.get_price() * item.quantity for item in self.items])
    
    def calculate_total(self):
        self.__calculate_price()
        self.__calculate_discount()
        self.__total = self.__subtotal - self.__discount

    def __calculate_discount(self):
        #50% discount if the price of the main beach exceeds $50,000
        if sum([item.get_price() * (item.quantity if isinstance(item, MainCourse) else 0) for item in self.items]) > 50000:
            self.__discount = sum([item.get_price() * (item.quantity if isinstance(item, Beverage) else 0) for item in self.items]) * 0.5
        
    def add_item(self, item):
        self.items.append(item)

    def print_bill(self):
        self.calculate_total()
        print("---------------")
        for item in self.items:
            print(f"{item.name} - {item.quantity} - {item.get_price()}")
        print("---------------")
        print("Descuento:", self.__discount)
        print(f"Total: {self.__total}")
        print("---------------")
    
    def pay_bill(self, money):
        if money.pay(self.__total):
            print("Thanks for your purchase, come back soon")
        else:
            self.pay_bill(money)

class Payment():
  def __init__(self):
    pass

  def pay(self, amount):
    pass

class Card(Payment):
  def __init__(self, number, cvv, password):
    super().__init__()
    self._number = number
    self._cvv = cvv
    self.__password = password

  def pay(self, amount):
    key = int(input("Enter your password: "))
    if key == self.__password:
        print(f"Paying {amount} with card {"******"+ str(self._number)[-4:]}")
        return True
    print("Incorrect password")
    return False

class Cash(Payment):
    def __init__(self, available):
        super().__init__()
        self._available = available

    def pay(self, amount):
        if self._available >= amount:
            print(f"Payment made in cash. Change: {self._available - amount}")
            return True
        else:
            print(f"Insufficient. {amount - self._available} are missing to complete the payment. You have to wash dishes!!!")
            return True



class MenuItem():
    def __init__(self, price, name, quantity) -> None:
        self.__price = price
        self.name = name
        self.quantity = quantity

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
    

class Beverage(MenuItem):
    def __init__(self, price, size, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.size = size
    def get_size(self):
        return self.size
    def set_size(self, new_size):
        self.size = new_size

class Appetizer(MenuItem):
    def __init__(self, price, customers, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.customers = customers
    def get_customers(self):
        return self.customers
    def set_customers(self, new_customers):
        self.customer = new_customers

class MainCourse(MenuItem):
    def __init__(self, price, grammage, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.grammage = grammage
    def get_grammage(self):
        return self.grammage
    def set_grammage(self, new_grammage):
        self.grammage = new_grammage


order = Order()
running = True

while running:
    selection = input("Would you like to order a main course? (y/n): ")
    if selection == "y":
        print("""Main Courses:
        1. Simple Burger
        2. Double Burger
        3. Ranch Burger
        4. All-Terrain Burger
        """)
        main_course = int(input("Select an option: "))
        if main_course == 1:
            print("Simple Burger selected")
            order.add_item(MainCourse(12000, 150, "Simple Burger", int(input("Quantity: "))))
        elif main_course == 2:
            print("Double Burger selected")
            order.add_item(MainCourse(16000, 300, "Double Burger", int(input("Quantity: "))))
        elif main_course == 3:
            print("Ranch Burger selected")
            order.add_item(MainCourse(20000, 200, "Ranch Burger", int(input("Quantity: "))))
        elif main_course == 4:
            print("All-Terrain Burger selected")
            order.add_item(MainCourse(23000, 250, "All-Terrain Burger", int(input("Quantity: "))))            

    selection = input("Would you like to order an appetizer? (y/n): ")
    if selection == "y":
        print("""Appetizers:
        1. Bread Basket (for 3 people)
        2. Soup (for 1 person)
        3. French Fries (for 5 people)
        """)
        appetizer = int(input("Select an option: "))
        if appetizer == 1:
            print("Bread Basket selected")
            order.add_item(Appetizer(4000, 3, "Bread Basket", int(input("Quantity: "))))
        elif appetizer == 2:
            print("Soup selected")
            order.add_item(Appetizer(6000, 1, "Soup", int(input("Quantity: "))))
        elif appetizer == 3:
            print("French Fries selected")
            order.add_item(Appetizer(8000, 5, "French Fries", int(input("Quantity: "))))

    selection = input("Would you like to order a beverage? (y/n): ")
    if selection == "y":
        print("""Beverages:
        1. Water
        2. Soda
        3. Juice
        """)
        beverage = int(input("Select an option: "))
        if beverage == 1:
            print("Water selected")
            order.add_item(Beverage(2000, 500, "Water", int(input("Quantity: "))))
        elif beverage == 2:
            print("Soda selected")
            order.add_item(Beverage(3000, 500, "Soda", int(input("Quantity: "))))
        elif beverage == 3:
            print("Juice selected")
            order.add_item(Beverage(5000, 600, "Juice", int(input("Quantity: "))))

    selection = input("Would you like to order anything else? (y/n): ")
    if selection == 'n':
        running = False



myCard = Card(number=1043706, cvv=122, password=2024)
myWallet = Cash(available=100000)


order.print_bill()
method = int(input("Pay with: 1. Card    2. Cash: "))
if method == 1:
    order.pay_bill(myCard)
elif method == 2:
    order.pay_bill(myWallet)
else:
    print("You have left without paying.")