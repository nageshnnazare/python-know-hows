"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - DESIGN PATTERNS
═══════════════════════════════════════════════════════════════════════

Common design patterns for solving recurring problems.
Topics: Creational, Structural, Behavioral patterns
"""

from abc import ABC, abstractmethod
from typing import List

print("="*70)
print("DESIGN PATTERNS")
print("="*70)

# ═══════════════════════════════════════════════════════════════════════
# CREATIONAL PATTERNS - Object creation
# ═══════════════════════════════════════════════════════════════════════

# 1. SINGLETON - Only one instance exists
print("--- Singleton Pattern ---")

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"Same instance: {s1 is s2}")

# 2. FACTORY - Create objects without specifying exact class
print("\n--- Factory Pattern ---")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal: {animal_type}")

dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")

# 3. BUILDER - Construct complex objects step by step
print("\n--- Builder Pattern ---")

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
    
    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("cheese")
        if self.pepperoni: toppings.append("pepperoni")
        if self.mushrooms: toppings.append("mushrooms")
        return f"{self.size} pizza with {', '.join(toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self
    
    def build(self):
        return self.pizza

pizza = (PizzaBuilder()
         .set_size("large")
         .add_cheese()
         .add_pepperoni()
         .build())
print(pizza)

# ═══════════════════════════════════════════════════════════════════════
# STRUCTURAL PATTERNS - Object composition
# ═══════════════════════════════════════════════════════════════════════

# 4. ADAPTER - Make incompatible interfaces work together
print("\n--- Adapter Pattern ---")

class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 110

class Adapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage()

eu_socket = EuropeanSocket()
adapter = Adapter(eu_socket)
print(f"Adapted voltage: {adapter.voltage()}V")

# 5. DECORATOR - Add behavior to objects dynamically
print("\n--- Decorator Pattern ---")

class Coffee:
    def cost(self):
        return 5
    
    def description(self):
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 1
    
    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 0.5
    
    def description(self):
        return self._coffee.description() + ", Sugar"

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")

# 6. FACADE - Simplified interface to complex subsystem
print("\n--- Facade Pattern ---")

class CPU:
    def freeze(self):
        print("CPU: Freezing")
    
    def execute(self):
        print("CPU: Executing")

class Memory:
    def load(self):
        print("Memory: Loading")

class HardDrive:
    def read(self):
        print("HardDrive: Reading")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start(self):
        """Simple interface for complex operation"""
        self.cpu.freeze()
        self.memory.load()
        self.hard_drive.read()
        self.cpu.execute()

computer = ComputerFacade()
computer.start()

# ═══════════════════════════════════════════════════════════════════════
# BEHAVIORAL PATTERNS - Object interaction
# ═══════════════════════════════════════════════════════════════════════

# 7. OBSERVER - Subscribe to events
print("\n--- Observer Pattern ---")

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} notified: state = {state}")

subject = Subject()
observer1 = Observer("Observer1")
observer2 = Observer("Observer2")

subject.attach(observer1)
subject.attach(observer2)
subject.set_state("Active")

# 8. STRATEGY - Select algorithm at runtime
print("\n--- Strategy Pattern ---")

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Simplified

class BubbleSort(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)  # Different strategy

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)

data = [3, 1, 4, 1, 5, 9, 2, 6]
sorter = Sorter(QuickSort())
print(f"QuickSort: {sorter.sort(data)}")

sorter.strategy = BubbleSort()
print(f"BubbleSort: {sorter.sort(data)}")

# 9. COMMAND - Encapsulate requests as objects
print("\n--- Command Pattern ---")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is ON")
    
    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

light = Light()
remote = RemoteControl()

remote.set_command(LightOnCommand(light))
remote.press_button()

remote.set_command(LightOffCommand(light))
remote.press_button()

# 10. ITERATOR - Traverse collection without exposing structure
print("\n--- Iterator Pattern ---")

class BookCollection:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def __iter__(self):
        return iter(self.books)

collection = BookCollection()
collection.add_book("Book 1")
collection.add_book("Book 2")
collection.add_book("Book 3")

for book in collection:
    print(f"Reading: {book}")

# 11. PATTERN SUMMARY
print("\n" + "="*70)
print("DESIGN PATTERNS SUMMARY")
print("="*70)

print("""
CREATIONAL (Object Creation):
  • Singleton: One instance only
  • Factory: Create objects without specifying class
  • Builder: Construct complex objects step-by-step
  • Prototype: Clone existing objects

STRUCTURAL (Object Composition):
  • Adapter: Make incompatible interfaces work
  • Decorator: Add behavior dynamically
  • Facade: Simplified interface to complex system
  • Proxy: Control access to objects

BEHAVIORAL (Object Interaction):
  • Observer: Subscribe to events
  • Strategy: Select algorithm at runtime
  • Command: Encapsulate requests as objects
  • Iterator: Traverse collections
  • State: Change behavior based on state

When to use:
  ✓ Solve recurring design problems
  ✓ Improve code maintainability
  ✓ Make code more flexible
  ✓ Common vocabulary for teams
  ✗ Don't over-engineer simple problems
""")

print("\n✓ Design patterns solve common problems")
print("✓ Use when appropriate, not everywhere")
print("✓ Understand the problem before applying pattern")
print("✓ Patterns improve code organization")
print("✓ Help communicate design decisions")

