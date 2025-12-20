"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - METACLASSES
═══════════════════════════════════════════════════════════════════════

Metaclasses are classes that create classes.
Topics: type(), __new__, __init__, class creation, use cases
"""

print("="*70)
print("METACLASSES - Classes of Classes")
print("="*70)

# 1. EVERYTHING IS AN OBJECT
print("--- Everything is an Object ---")
class MyClass:
    pass

obj = MyClass()
print(f"obj type: {type(obj)}")           # MyClass
print(f"MyClass type: {type(MyClass)}")   # type (metaclass!)
print(f"type type: {type(type)}")         # type

# 2. CREATING CLASSES DYNAMICALLY
print("\n--- Dynamic Class Creation ---")

# Using type() to create a class
MyDynamicClass = type('MyDynamicClass', (), {'x': 5})
obj = MyDynamicClass()
print(f"Dynamic class attribute: {obj.x}")

# With methods
def greet(self):
    return "Hello!"

Person = type('Person', (), {'greet': greet})
p = Person()
print(f"Dynamic method: {p.greet()}")

# 3. CUSTOM METACLASS
print("\n--- Custom Metaclass ---")

class Meta(type):
    """Custom metaclass"""
    
    def __new__(mcs, name, bases, attrs):
        print(f"Creating class: {name}")
        attrs['created_by'] = 'Meta'
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

print(f"Created by: {MyClass.created_by}")

# 4. SINGLETON PATTERN
print("\n--- Singleton with Metaclass ---")

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    pass

db1 = Database()
db2 = Database()
print(f"Same instance: {db1 is db2}")

# 5. VALIDATION METACLASS
print("\n--- Attribute Validation ---")

class ValidatedMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Ensure class has required attributes
        if 'validate' not in attrs:
            attrs['validate'] = lambda self: True
        return super().__new__(mcs, name, bases, attrs)

class ValidatedClass(metaclass=ValidatedMeta):
    pass

obj = ValidatedClass()
print(f"Has validate: {hasattr(obj, 'validate')}")

print("\n✓ Metaclasses control class creation")
print("✓ type is the default metaclass")
print("✓ Use for framework-level features")
print("✓ Rarely needed in application code")

