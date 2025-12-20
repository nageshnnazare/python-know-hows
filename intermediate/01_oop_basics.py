"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - OBJECT-ORIENTED PROGRAMMING BASICS
═══════════════════════════════════════════════════════════════════════

Object-Oriented Programming (OOP) organizes code around objects and classes.
In this module, you'll learn about:
- Classes and objects
- Attributes and methods
- __init__ constructor
- Instance vs class variables
- self parameter
- String representation methods
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. CLASSES AND OBJECTS - The Foundation
# ═══════════════════════════════════════════════════════════════════════

"""
Class: Blueprint for creating objects
Object: Instance of a class

    ┌─────────────────┐
    │  Class: Dog     │  ← Blueprint
    ├─────────────────┤
    │  - name         │
    │  - age          │
    │  - bark()       │
    └─────────────────┘
           │
      Creates ▼
    ┌─────────────────┐
    │ Object: my_dog  │  ← Instance
    │ name = "Buddy"  │
    │ age = 3         │
    └─────────────────┘
"""

print("="*70)
print("1. CLASSES AND OBJECTS")
print("="*70)

# Define a simple class
class Dog:
    """A simple Dog class"""
    pass

# Create objects (instances)
dog1 = Dog()
dog2 = Dog()

print(f"dog1: {dog1}")
print(f"dog2: {dog2}")
print(f"Are they the same? {dog1 is dog2}")


# ═══════════════════════════════════════════════════════════════════════
# 2. ATTRIBUTES - Object Data
# ═══════════════════════════════════════════════════════════════════════

"""
Attributes are variables that belong to an object
"""

print("\n" + "="*70)
print("2. ATTRIBUTES")
print("="*70)

# Adding attributes to an object
dog = Dog()
dog.name = "Buddy"
dog.age = 3
dog.breed = "Golden Retriever"

print(f"Name: {dog.name}")
print(f"Age: {dog.age}")
print(f"Breed: {dog.breed}")


# ═══════════════════════════════════════════════════════════════════════
# 3. METHODS - Object Behavior
# ═══════════════════════════════════════════════════════════════════════

"""
Methods are functions that belong to a class
"""

print("\n" + "="*70)
print("3. METHODS")
print("="*70)

class Dog:
    """Dog class with methods"""
    
    def bark(self):
        """Make the dog bark"""
        print("Woof! Woof!")
    
    def sit(self):
        """Make the dog sit"""
        print("The dog is sitting")

# Create and use methods
my_dog = Dog()
my_dog.name = "Buddy"

print(f"{my_dog.name} is barking:")
my_dog.bark()
my_dog.sit()


# ═══════════════════════════════════════════════════════════════════════
# 4. THE __init__ METHOD - Constructor
# ═══════════════════════════════════════════════════════════════════════

"""
__init__ is called when creating a new object (constructor)

    ┌────────────────────────────┐
    │  dog = Dog("Buddy", 3)     │
    └────────────────────────────┘
              │
              ▼
    ┌────────────────────────────┐
    │  __init__(self, name, age) │  ← Automatically called
    └────────────────────────────┘
"""

print("\n" + "="*70)
print("4. THE __init__ METHOD")
print("="*70)

class Dog:
    """Dog class with constructor"""
    
    def __init__(self, name, age, breed="Mixed"):
        """Initialize a new Dog"""
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        """Make the dog bark"""
        print(f"{self.name} says: Woof!")
    
    def get_info(self):
        """Return dog information"""
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Create dogs using constructor
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5)  # Uses default breed

print(dog1.get_info())
print(dog2.get_info())

dog1.bark()
dog2.bark()


# ═══════════════════════════════════════════════════════════════════════
# 5. UNDERSTANDING 'self'
# ═══════════════════════════════════════════════════════════════════════

"""
'self' represents the instance of the class
- First parameter of instance methods
- Gives access to attributes and methods
- Python passes it automatically

    dog.bark()  → Dog.bark(dog)
                      ↑
                    self
"""

print("\n" + "="*70)
print("5. UNDERSTANDING 'self'")
print("="*70)

class Counter:
    """A simple counter class"""
    
    def __init__(self, start=0):
        self.count = start  # self.count is instance attribute
    
    def increment(self):
        self.count += 1     # Access instance attribute
        return self.count
    
    def reset(self):
        self.count = 0

counter = Counter(10)
print(f"Initial count: {counter.count}")
print(f"After increment: {counter.increment()}")
print(f"After increment: {counter.increment()}")
counter.reset()
print(f"After reset: {counter.count}")


# ═══════════════════════════════════════════════════════════════════════
# 6. INSTANCE VS CLASS VARIABLES
# ═══════════════════════════════════════════════════════════════════════

"""
Instance variables: Unique to each instance (use self.)
Class variables: Shared by all instances

    ┌──────────────────────────────────┐
    │  Class: Dog                      │
    │  species = "Canis familiaris"    │  ← Class variable (shared)
    └──────────────────────────────────┘
              │
       Creates│
              ▼
    ┌──────────────────┐    ┌──────────────────┐
    │  dog1            │    │  dog2            │
    │  name = "Buddy"  │    │  name = "Max"    │  ← Instance variables
    │  age = 3         │    │  age = 5         │     (unique)
    └──────────────────┘    └──────────────────┘
"""

print("\n" + "="*70)
print("6. INSTANCE VS CLASS VARIABLES")
print("="*70)

class Dog:
    """Dog class demonstrating class and instance variables"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    count = 0  # Track number of dogs created
    
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        Dog.count += 1  # Increment class variable
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1: {dog1.get_info()}")
print(f"dog2: {dog2.get_info()}")
print(f"Total dogs created: {Dog.count}")
print(f"Species (from class): {Dog.species}")
print(f"Species (from instance): {dog1.species}")


# ═══════════════════════════════════════════════════════════════════════
# 7. STRING REPRESENTATION
# ═══════════════════════════════════════════════════════════════════════

"""
Special methods for string representation:
- __str__:  Human-readable (for users)
- __repr__: Unambiguous (for developers)
"""

print("\n" + "="*70)
print("7. STRING REPRESENTATION")
print("="*70)

class Dog:
    """Dog class with string representations"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """String for print() and str()"""
        return f"Dog named {self.name}, age {self.age}"
    
    def __repr__(self):
        """String for repr() and interactive shell"""
        return f"Dog(name='{self.name}', age={self.age})"

dog = Dog("Buddy", 3)

print(f"str(dog): {str(dog)}")      # Calls __str__
print(f"repr(dog): {repr(dog)}")    # Calls __repr__
print(f"print(dog): ", end="")
print(dog)                          # Calls __str__


# ═══════════════════════════════════════════════════════════════════════
# 8. PRACTICAL EXAMPLE: BANK ACCOUNT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("8. PRACTICAL EXAMPLE: BANK ACCOUNT")
print("="*70)

class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, owner, balance=0):
        """Initialize account with owner and optional balance"""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive")
    
    def get_balance(self):
        """Return current balance"""
        return self.balance
    
    def __str__(self):
        return f"Account[{self.owner}]: ${self.balance}"

# Using the BankAccount class
account = BankAccount("Alice", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Insufficient funds
print(f"Final balance: ${account.get_balance()}")


# ═══════════════════════════════════════════════════════════════════════
# 9. PRACTICAL EXAMPLE: SHOPPING CART
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("9. PRACTICAL EXAMPLE: SHOPPING CART")
print("="*70)

class Product:
    """Represents a product"""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class ShoppingCart:
    """Represents a shopping cart"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        """Add product to cart"""
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity}x {product.name}")
    
    def remove_item(self, product_name):
        """Remove product from cart"""
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name}")
                return
        print(f"{product_name} not found in cart")
    
    def get_total(self):
        """Calculate total price"""
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def show_cart(self):
        """Display cart contents"""
        print("\n--- Shopping Cart ---")
        if not self.items:
            print("Cart is empty")
            return
        
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            print(f"{product.name} x{quantity}: ${subtotal:.2f}")
        
        print(f"Total: ${self.get_total():.2f}")

# Using the shopping cart
cart = ShoppingCart()

laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 25.50)
keyboard = Product("Keyboard", 75.00)

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)

cart.show_cart()

cart.remove_item("Mouse")
cart.show_cart()


# ═══════════════════════════════════════════════════════════════════════
# 10. CLASS METHODS AND STATIC METHODS
# ═══════════════════════════════════════════════════════════════════════

"""
Instance method: Works with instance (uses self)
Class method:    Works with class (uses cls)
Static method:   Independent (no self or cls)
"""

print("\n" + "="*70)
print("10. CLASS METHODS AND STATIC METHODS")
print("="*70)

class Employee:
    """Employee class demonstrating different method types"""
    
    company = "TechCorp"
    num_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1
    
    # Instance method
    def give_raise(self, amount):
        """Give raise to this employee"""
        self.salary += amount
        print(f"{self.name} got a ${amount} raise!")
    
    # Class method
    @classmethod
    def get_employee_count(cls):
        """Return number of employees"""
        return cls.num_employees
    
    @classmethod
    def set_company_name(cls, name):
        """Change company name"""
        cls.company = name
    
    # Static method
    @staticmethod
    def is_workday(day):
        """Check if day is a workday"""
        return day not in ["Saturday", "Sunday"]
    
    def __str__(self):
        return f"{self.name} ({self.company}): ${self.salary}"

# Using different method types
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1)
print(emp2)

# Instance method
emp1.give_raise(5000)
print(emp1)

# Class method
print(f"\nTotal employees: {Employee.get_employee_count()}")
Employee.set_company_name("MegaCorp")
print(f"Company: {Employee.company}")

# Static method
print(f"\nIs Monday a workday? {Employee.is_workday('Monday')}")
print(f"Is Saturday a workday? {Employee.is_workday('Saturday')}")


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Create a Rectangle class with:
   - __init__(width, height)
   - area() method
   - perimeter() method
   - __str__() method

2. Create a Student class with:
   - name, age, grades (list)
   - add_grade(grade) method
   - get_average() method
   - is_passing() method (average >= 60)

3. Create a Book class with:
   - title, author, pages, current_page
   - read(pages) method
   - is_finished() method
   - Class variable to count total books

4. Create a Temperature class with:
   - __init__(celsius)
   - to_fahrenheit() method
   - to_kelvin() method
   - @classmethod from_fahrenheit(f)
   - @staticmethod is_freezing(celsius)

5. Create a Circle class with:
   - radius
   - area() and circumference() methods
   - __str__() and __repr__()
   - Class variable for PI

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Classes are blueprints, objects are instances
✓ __init__ initializes new objects
✓ self represents the instance
✓ Instance variables: unique to each object
✓ Class variables: shared by all objects
✓ Methods are functions in a class
✓ __str__ for user-friendly representation
✓ __repr__ for developer representation
✓ @classmethod works with class
✓ @staticmethod is independent

Next up: 02_oop_advanced.py - Inheritance and more!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

# Solution 2:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self):
        return self.get_average() >= 60

# Solution 3:
class Book:
    total_books = 0
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        Book.total_books += 1
    
    def read(self, pages):
        self.current_page = min(self.current_page + pages, self.pages)
    
    def is_finished(self):
        return self.current_page >= self.pages

# Solution 4:
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5/9
        return cls(celsius)
    
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0

# Solution 5:
class Circle:
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
    
    def circumference(self):
        return 2 * Circle.PI * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
"""

