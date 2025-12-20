"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - DESCRIPTORS
═══════════════════════════════════════════════════════════════════════

Descriptors control attribute access.
Topics: __get__, __set__, __delete__, property implementation
"""

print("="*70)
print("DESCRIPTORS")
print("="*70)

# 1. DESCRIPTOR PROTOCOL
print("--- Basic Descriptor ---")

class Descriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        print(f"Getting {self.name}")
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj, value):
        print(f"Setting {self.name} to {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        print(f"Deleting {self.name}")
        del obj.__dict__[self.name]

class MyClass:
    attr = Descriptor('attr')

obj = MyClass()
obj.attr = 42
print(obj.attr)
del obj.attr

# 2. VALIDATION DESCRIPTOR
print("\n--- Validation ---")

class PositiveNumber:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class BankAccount:
    balance = PositiveNumber('balance')
    
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(100)
print(f"Balance: {account.balance}")

try:
    account.balance = -50
except ValueError as e:
    print(f"Error: {e}")

# 3. TYPED DESCRIPTOR
print("\n--- Type Checking ---")

class TypedField:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}"
            )
        obj.__dict__[self.name] = value

class Person:
    name = TypedField('name', str)
    age = TypedField('age', int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(f"{person.name}, {person.age}")

# 4. HOW @property WORKS
print("\n--- Property Descriptor ---")

class Property:
    """Simplified property implementation"""
    
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)
    
    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

print("✓ Descriptors control attribute access")
print("✓ __get__, __set__, __delete__ methods")
print("✓ Used to implement @property")
print("✓ Great for validation and type checking")

