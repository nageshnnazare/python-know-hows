"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - ADVANCED OOP
═══════════════════════════════════════════════════════════════════════

Advanced Object-Oriented Programming concepts.
In this module, you'll learn about:
- Inheritance
- Method overriding
- super()
- Multiple inheritance
- Polymorphism
- Encapsulation (public, protected, private)
- Property decorators
- Abstract base classes
"""

from abc import ABC, abstractmethod

# ═══════════════════════════════════════════════════════════════════════
# 1. INHERITANCE - Building on Existing Classes
# ═══════════════════════════════════════════════════════════════════════

"""
Inheritance allows a class to inherit attributes and methods from another class

    ┌──────────────────┐
    │   Animal         │  ← Parent/Base/Super class
    │   - name         │
    │   - speak()      │
    └──────────────────┘
            ▲
            │ inherits
    ┌───────┴────────┐
    │                │
┌───┴───┐      ┌─────┴───┐
│  Dog  │      │   Cat   │  ← Child/Derived/Sub classes
└───────┘      └─────────┘
"""

print("="*70)
print("1. INHERITANCE")
print("="*70)

# Base class
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        """Make animal sound"""
        print(f"{self.name} makes a sound")
    
    def info(self):
        """Display animal info"""
        return f"{self.name} is {self.age} years old"

# Derived classes
class Dog(Animal):
    """Dog class inherits from Animal"""
    
    def speak(self):
        """Override speak method"""
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    """Cat class inherits from Animal"""
    
    def speak(self):
        """Override speak method"""
        print(f"{self.name} says: Meow!")

# Using inheritance
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 5)

print(dog.info())  # Inherited from Animal
dog.speak()        # Overridden in Dog

print(cat.info())  # Inherited from Animal
cat.speak()        # Overridden in Cat


# ═══════════════════════════════════════════════════════════════════════
# 2. SUPER() - Accessing Parent Class
# ═══════════════════════════════════════════════════════════════════════

"""
super() allows you to call methods from the parent class
"""

print("\n" + "="*70)
print("2. SUPER() - ACCESSING PARENT CLASS")
print("="*70)

class Animal:
    """Base class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Animal.__init__ called for {name}")
    
    def describe(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class with additional attributes"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent's __init__
        self.breed = breed
        print(f"Dog.__init__ called for {name}")
    
    def describe(self):
        """Override and extend parent method"""
        base_desc = super().describe()  # Call parent's describe
        return f"{base_desc}, breed: {self.breed}"

dog = Dog("Max", 4, "Labrador")
print(dog.describe())


# ═══════════════════════════════════════════════════════════════════════
# 3. MULTIPLE INHERITANCE
# ═══════════════════════════════════════════════════════════════════════

"""
A class can inherit from multiple parent classes

    ┌─────────┐      ┌─────────┐
    │  Parent1│      │ Parent2 │
    └────┬────┘      └────┬────┘
         │                │
         └────────┬───────┘
                  │
            ┌─────┴─────┐
            │   Child   │  ← Inherits from both
            └───────────┘
"""

print("\n" + "="*70)
print("3. MULTIPLE INHERITANCE")
print("="*70)

class Flyable:
    """Mixin for flying ability"""
    
    def fly(self):
        print(f"{self.name} is flying!")

class Swimmable:
    """Mixin for swimming ability"""
    
    def swim(self):
        print(f"{self.name} is swimming!")

class Duck(Animal, Flyable, Swimmable):
    """Duck can do everything!"""
    
    def speak(self):
        print(f"{self.name} says: Quack!")
    
    def info(self):
        """Provide duck info"""
        return f"{self.name} is a {self.age}-year-old duck"

duck = Duck("Donald", 2)
print(duck.info())    # From Duck (with Animal attributes)
duck.speak()          # Overridden
duck.fly()            # From Flyable
duck.swim()           # From Swimmable

# Method Resolution Order (MRO)
print(f"\nMRO: {Duck.__mro__}")


# ═══════════════════════════════════════════════════════════════════════
# 4. POLYMORPHISM - One Interface, Multiple Forms
# ═══════════════════════════════════════════════════════════════════════

"""
Polymorphism allows different classes to be used through the same interface
"""

print("\n" + "="*70)
print("4. POLYMORPHISM")
print("="*70)

class Shape:
    """Base shape class"""
    
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
    
    def perimeter(self):
        return 2 * Circle.PI * self.radius

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(10, 2)
]

print("--- Shape Information ---")
for shape in shapes:
    # Same interface (area and perimeter) but different implementations!
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, "
          f"Perimeter = {shape.perimeter():.2f}")


# ═══════════════════════════════════════════════════════════════════════
# 5. ENCAPSULATION - Public, Protected, Private
# ═══════════════════════════════════════════════════════════════════════

"""
Encapsulation controls access to attributes and methods:

    public:     accessible everywhere (name)
    protected:  indicated by single underscore (_name)
    private:    indicated by double underscore (__name)
"""

print("\n" + "="*70)
print("5. ENCAPSULATION")
print("="*70)

class BankAccount:
    """Bank account with encapsulation"""
    
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_number = "12345"  # Protected (convention)
        self.__balance = balance        # Private (name mangling)
    
    def deposit(self, amount):
        """Public method"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
    
    def get_balance(self):
        """Public method to access private attribute"""
        return self.__balance
    
    def __process_transaction(self):
        """Private method"""
        print("Processing transaction...")

account = BankAccount("Alice", 1000)

# Public access
print(f"Owner: {account.owner}")

# Protected access (not enforced, just convention)
print(f"Account number: {account._account_number}")

# Private access (name mangled to _ClassName__attribute)
# print(account.__balance)  # Would raise AttributeError
print(f"Balance (via method): {account.get_balance()}")

# Accessing private (not recommended!)
print(f"Balance (via mangled name): {account._BankAccount__balance}")


# ═══════════════════════════════════════════════════════════════════════
# 6. PROPERTY DECORATORS - Getter, Setter, Deleter
# ═══════════════════════════════════════════════════════════════════════

"""
Properties provide controlled access to attributes
"""

print("\n" + "="*70)
print("6. PROPERTY DECORATORS")
print("="*70)

class Person:
    """Person with property decorators"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name"""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        """Getter for age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    @age.deleter
    def age(self):
        """Deleter for age"""
        print("Deleting age")
        del self._age

person = Person("Alice", 25)

# Using properties (looks like attribute access)
print(f"Name: {person.name}")
print(f"Age: {person.age}")

# Setting with validation
person.age = 30
print(f"New age: {person.age}")

try:
    person.age = 200  # Validation error!
except ValueError as e:
    print(f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════
# 7. ABSTRACT BASE CLASSES
# ═══════════════════════════════════════════════════════════════════════

"""
Abstract Base Classes (ABC) define interfaces that subclasses must implement
"""

print("\n" + "="*70)
print("7. ABSTRACT BASE CLASSES")
print("="*70)

class Vehicle(ABC):
    """Abstract base class for vehicles"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def stop(self):
        """Abstract method"""
        pass
    
    def display_info(self):
        """Concrete method (optional to override)"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Concrete implementation of Vehicle"""
    
    def start(self):
        return f"{self.brand} {self.model} engine started"
    
    def stop(self):
        return f"{self.brand} {self.model} engine stopped"

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} kick started"
    
    def stop(self):
        return f"{self.brand} {self.model} stopped"

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic", "Model")  # Would raise TypeError

# Can instantiate concrete classes
car = Car("Toyota", "Camry")
print(car.display_info())
print(car.start())
print(car.stop())

motorcycle = Motorcycle("Harley", "Davidson")
print(f"\n{motorcycle.display_info()}")
print(motorcycle.start())


# ═══════════════════════════════════════════════════════════════════════
# 8. PRACTICAL EXAMPLE: Employee System
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("8. PRACTICAL EXAMPLE: EMPLOYEE SYSTEM")
print("="*70)

class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self._salary = salary  # Protected
    
    @property
    def salary(self):
        return self._salary
    
    def calculate_bonus(self):
        """Calculate annual bonus (10% of salary)"""
        return self._salary * 0.10
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (ID: {self.employee_id})"

class Manager(Employee):
    """Manager with team management"""
    
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    
    def calculate_bonus(self):
        """Managers get 20% bonus + $1000 per team member"""
        base_bonus = self._salary * 0.20
        team_bonus = self.team_size * 1000
        return base_bonus + team_bonus

class Developer(Employee):
    """Developer with programming languages"""
    
    def __init__(self, name, employee_id, salary, languages):
        super().__init__(name, employee_id, salary)
        self.languages = languages
    
    def calculate_bonus(self):
        """Developers get 15% bonus + $500 per language"""
        base_bonus = self._salary * 0.15
        language_bonus = len(self.languages) * 500
        return base_bonus + language_bonus

# Create employees
employees = [
    Manager("Alice", "M001", 100000, team_size=5),
    Developer("Bob", "D001", 80000, languages=["Python", "JavaScript", "Java"]),
    Developer("Charlie", "D002", 75000, languages=["Python", "Go"])
]

print("--- Employee Information ---")
for emp in employees:
    print(f"{emp}")
    print(f"  Salary: ${emp.salary:,}")
    print(f"  Bonus: ${emp.calculate_bonus():,.2f}")
    print()


# ═══════════════════════════════════════════════════════════════════════
# 9. MAGIC METHODS (Dunder Methods)
# ═══════════════════════════════════════════════════════════════════════

"""
Magic methods allow customization of built-in behavior
"""

print("="*70)
print("9. MAGIC METHODS")
print("="*70)

class Vector:
    """2D Vector with magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Vector addition"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Vector subtraction"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Magnitude"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """Index access"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES")
print("="*70)

"""
1. Create a base class Shape with area() and perimeter() methods
   Then create Triangle and Square subclasses

2. Create an abstract class Payment with process() method
   Implement CreditCard and PayPal classes

3. Create a Person class with name and age properties
   Add validation: name must not be empty, age must be positive

4. Create a class Complex for complex numbers with:
   - __add__, __sub__, __mul__
   - __str__ and __repr__
   - magnitude() method

5. Create a hierarchy:
   - Animal (base)
   - Mammal (inherits Animal, adds fur_color)
   - Dog (inherits Mammal, adds breed)
   Use super() in all __init__ methods

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Inheritance: class Child(Parent)
✓ super() calls parent class methods
✓ Multiple inheritance: class Child(Parent1, Parent2)
✓ Polymorphism: same interface, different implementations
✓ Encapsulation: public, _protected, __private
✓ @property for getters/setters
✓ ABC for abstract base classes
✓ Magic methods customize behavior
✓ Method Resolution Order (MRO)
✓ Use composition over inheritance when appropriate

Next: 03_exception_handling.py
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

# Solution 2:
class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPal(Payment):
    def process(self, amount):
        return f"Processing ${amount} via PayPal"

# Solution 3:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value

# Solution 4:
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.real}+{self.imag}j"
    
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

# Solution 5:
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed
"""

