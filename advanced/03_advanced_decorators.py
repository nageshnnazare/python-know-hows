"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - ADVANCED DECORATORS
═══════════════════════════════════════════════════════════════════════

Advanced decorator patterns and techniques.
Topics: decorator classes, stacking, preserving metadata
"""

from functools import wraps, lru_cache
import time

print("="*70)
print("ADVANCED DECORATORS")
print("="*70)

# 1. CLASS AS DECORATOR
print("--- Class-Based Decorator ---")

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
print(f"Total calls: {greet.count}")

# 2. DECORATOR WITH STATE
print("\n--- Stateful Decorator ---")

def rate_limit(max_per_second):
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < 1.0 / max_per_second:
                time.sleep(1.0 / max_per_second - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limit(2)  # Max 2 calls per second
def api_call():
    print("API called")

# 3. DECORATOR FACTORY
print("\n--- Decorator Factory ---")

def debug(prefix="DEBUG"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix}: {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

@debug("TRACE")
def add(a, b):
    return a + b

add(5, 3)

# 4. CONDITIONAL DECORATOR
print("\n--- Conditional Execution ---")

def run_if(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Skipping {func.__name__}")
                return None
        return wrapper
    return decorator

DEBUG = True

@run_if(DEBUG)
def debug_function():
    print("Debug mode enabled")

debug_function()

# 5. RETRY DECORATOR
print("\n--- Retry Decorator ---")

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt+1} failed, retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success"

try:
    result = unreliable_function()
    print(f"Result: {result}")
except Exception as e:
    print(f"Failed after retries: {e}")

# 6. BUILT-IN DECORATORS
print("\n--- Built-in Decorators ---")

# @lru_cache for memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Cache info: {fibonacci.cache_info()}")

# 7. PROPERTY DECORATORS
print("\n--- Property Decorators ---")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

print("\n✓ Decorators can be classes")
print("✓ Use functools.wraps to preserve metadata")
print("✓ Decorator factories return decorators")
print("✓ @lru_cache for automatic memoization")
print("✓ Combine multiple decorators")

