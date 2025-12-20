"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - DECORATORS
═══════════════════════════════════════════════════════════════════════

Decorators modify or enhance functions/classes without changing their code.
Topics: function decorators, class decorators, built-in decorators
"""

import time
from functools import wraps

print("="*70)
print("DECORATORS")
print("="*70)

# 1. BASIC DECORATOR
print("--- Basic Decorator ---")

def my_decorator(func):
    """Simple decorator"""
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Wrapped version

# 2. DECORATOR WITH ARGUMENTS
print("\n--- Decorator with Arguments ---")

def smart_decorator(func):
    @wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result: {result}")

# 3. TIMING DECORATOR
print("\n--- Timing Decorator ---")

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# 4. LOGGING DECORATOR
print("\n--- Logging Decorator ---")

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")
greet("Bob", greeting="Hi")

# 5. DECORATOR WITH PARAMETERS
print("\n--- Decorator with Parameters ---")

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()

# 6. CLASS DECORATORS
print("\n--- Class Decorators ---")

def singleton(cls):
    """Ensure only one instance of class exists"""
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creating Database instance")

db1 = Database()
db2 = Database()
print(f"Same instance? {db1 is db2}")

# 7. MULTIPLE DECORATORS
print("\n--- Multiple Decorators ---")

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# 8. BUILT-IN DECORATORS
print("\n--- Built-in Decorators ---")

class MyClass:
    class_var = "class variable"
    
    def instance_method(self):
        """Regular instance method"""
        return "instance method"
    
    @classmethod
    def class_method(cls):
        """Works with class, not instance"""
        return cls.class_var
    
    @staticmethod
    def static_method():
        """Independent of class and instance"""
        return "static method"
    
    @property
    def computed(self):
        """Access like attribute"""
        return "computed property"

obj = MyClass()
print(f"Instance: {obj.instance_method()}")
print(f"Class: {MyClass.class_method()}")
print(f"Static: {MyClass.static_method()}")
print(f"Property: {obj.computed}")

# 9. PRACTICAL EXAMPLES
print("\n--- Cache Decorator ---")

def memoize(func):
    """Cache function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")

print("\n✓ Decorators add functionality without modifying code")
print("✓ Use @wraps to preserve function metadata")
print("✓ Can stack multiple decorators")
print("✓ Common uses: logging, timing, caching")
print("✓ @property, @classmethod, @staticmethod are built-in")

